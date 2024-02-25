#!/usr/bin/env python3

"""
gamin-backup is a script to download your activities from 
Garmin Connect, so you can keep a local copy in your computer.

Usage: garmin-backup [options] <path>

  <path>                    Activity folder to store your activities.


Options:
  -f, --formats=FORMAT      Which formats to download [default: gpx].
                            Choose from the available options: 
                            original|gpx|csv|tcx|kml. You can have more than 
                            one format by separating them by spaces, and in "".
  -u, --username=USERNAME   Username of your Garmin account
  -p, --password=PASSWORD   Password of your Garmin account
  -a, --activity=ID         Activity ID. Download only that activity, even 
                            if it has already been downloaded. Yoy can add
                            several IDs separated by space, and in "".
  -s, --start=S_DATE        Start date, in ISO format. If only the year is
                            provided, it will assume Jan 1st of that year.
  -e, --end=e_DATE          End date, in ISO format. If only the year is
                            provided, it will assume Dec 31st of that year.
  --fake                    Use fake data, instead of connecting to Garmin.
                            For test purposes only.
  --help                    Show this message and exit.
  --verion                  Show the version and exit.

The username and password can also be provided through environment variables 
USER and PASSWORD. If not provided through command line or environment 
variables, the program will prompt for this information the first time. The 
credential information will then be stored in .garminconnect folder, and re-used 
for the future, until they need to be refreshed.

All activities between S_DATE and E_DATE that are not already present in <path> 
will be downloaded. If no dates are provided, it will assume all activities, 
from the beginning until today.

There is a limit of 100 activities at a time, in order to avoid overloading
the Garmin Connect page, and getting banned. If you have more than 100 
activities to download, you can just run the program again.
"""

import datetime
import logging
import os

from getpass import getpass
import requests
from garth.exc import GarthHTTPError
from docopt import docopt

from garminconnect import Garmin, GarminConnectAuthenticationError

from activities import activities


__version__ = 0.5
BASE_PATH = os.path.dirname(__file__)
TOKEN_STORE_DIR = os.path.join(BASE_PATH, ".garminconnect")
MAX_ACTIVITIES = 100

# Configure debug logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FakeGarmin:
    """used to test without connecting to Garmin"""
    def get_activities(self, start:int, limit:int):
        return activities


    def get_activities_by_date(self, startdate: datetime.date, enddate: datetime.date, activitytype:str=None):
        """get activities between dates"""

        idx = []
        for i, activity in enumerate(activities):
            date = datetime.datetime.fromisoformat(activity['startTimeLocal'])
            if startdate <= date.date() <= enddate:
                idx.append(i)
        
        return [ activities[i] for i in idx ]


    def download_activity(self, activity_id:str, dl_fmt=Garmin.ActivityDownloadFormat.GPX):
        """Download activity requested in requested format"""
        return f"Activity {activity_id}: long string of characters...".encode()



def get_credentials():
    """Get user credentials."""

    user = input("Login user: ")
    password = getpass("Enter password: ")

    return user, password


def init_api(user: str, password: str, tokenstore: str) -> Garmin:
    """initialise session with Garmin, return a Garmin API object"""

    try:
        # Using Oauth1 and OAuth2 token files from directory
        print(
            f"Trying to login to Garmin Connect using token data from directory '{tokenstore}'...\n"
        )

        garmin = Garmin()
        garmin.login(tokenstore)

    except (FileNotFoundError, GarthHTTPError, GarminConnectAuthenticationError):
        # Session is expired. You'll need to log in again
        print(
            "Login tokens not present, login with your Garmin Connect credentials to generate them.\n"
            f"They will be stored in '{tokenstore}' for future use.\n"
        )
        try:
            # Ask for credentials if not set as environment variables
            if not user or not password:
                user, password = get_credentials()

            garmin = Garmin(user, password)
            garmin.login()
            # Save Oauth1 and Oauth2 token files to directory for next login
            garmin.garth.dump(tokenstore)
            print(
                f"Oauth tokens stored in '{tokenstore}' directory for future use. (first method)\n"
            )
        except (FileNotFoundError, GarthHTTPError, GarminConnectAuthenticationError, requests.exceptions.HTTPError) as err:
            logger.error(err)
            return None

    return garmin


def parse_date(date: str, date_type='start') -> datetime.date:
    """
    check if a year is provided, or a date, and 
    transform it to datetime.date
    """
    # if it's a year
    if len(date) == 4:
        year = int(date)
        if date_type == 'start':
            return datetime.date(year, 1, 1)
        else:
            return datetime.date(year, 12, 31)
    
    # if it's an ISO date
    else:
        return datetime.datetime.fromisoformat(date).date

    

def parse_arguments(arguments: dict[str: str]) -> dict:
    """parse command line arguments, return arguments parsed"""
    args = arguments.copy()

    # dates parsing
    if args['--end']:
        args['--end'] = parse_date(args['--end'], date_type='end')
    else:
        args['--end'] = datetime.date.today()  # latest date possible

    if args['--start']:
        args['--start'] = parse_date(args['--start'], date_type='start')
    else:
        args['--start'] = datetime.date(1900, 1, 1)  # just a very early date
    

    # format parsing
    args['--formats'] = args['--formats'].lower().split()
    for format in args['--formats']:
        if format not in ['original', 'gpx', 'csv', 'tcx', 'kml']:
            raise Exception("Invalid format. Type garmin-backup --help for more information")
    
    # activities parsing
    if args['--activity']:
        args['--activity'] = args['--activity'].split()

    return args


def generate_activity_name(date: str, name:str) -> str:
    """return name of the activity file, built from the parameters"""
    prefix = date.replace(':', '').replace(' ', '_')[:-2]
    suffix = name.replace(' ', '_')
    return f'{prefix}-{suffix}'


def get_download_activities(path: str, start: datetime.date, end: datetime.date, api: Garmin) -> list[str]:
    """return list of activity ids that need to be downloaded"""
    
    # get activity names already in disk -- put in a set to remove duplicates
    files = os.listdir(path)
    disk_activities = {file.split('.')[0] for file in files}

    # get all activities available in garmin
    garmin_activities = api.get_activities_by_date(start, end)
    garmin_activities = [
        {
            'name': generate_activity_name(a["startTimeLocal"], a["activityName"]),
            'id': a["activityId"]
        }
        for a in garmin_activities
    ]

    # download activities are those that are not in disk already
    download_activities = [
        activity
        for activity in garmin_activities
        if activity['name'] not in disk_activities
    ]

    # trunkate list if it exceeds the maximum allowed
    if len(download_activities) > MAX_ACTIVITIES:
        download_activities = download_activities[:MAX_ACTIVITIES]

    return download_activities


def download_activities(
    activities: list[dict], formats: list[str], api:Garmin
) -> None:
    """
    download the activities from the list provided, and write
    files in disk. The list is a list of acitivities containing
    the 'id' and the 'name' for each activity.
    """

    for activity in activities:
        for file_format in formats:
            ext = 'zip' if file_format=="original" else file_format
            filename = f"{activity['name']}.{ext}"
            print(f"Downloading {filename}...")
            match file_format:
                case 'gpx':
                    dl_fmt = Garmin.ActivityDownloadFormat.GPX
                case 'tcx':
                    dl_fmt = Garmin.ActivityDownloadFormat.TCX
                case 'kml':
                    dl_fmt = Garmin.ActivityDownloadFormat.KML
                case 'csv':
                    dl_fmt = Garmin.ActivityDownloadFormat.CSV
                case 'original':
                    dl_fmt = Garmin.ActivityDownloadFormat.ORIGINAL

            data = api.download_activity(
                activity['id'], dl_fmt=dl_fmt
            )
            fullname = os.path.join(args['<path>'], filename)
            with open(fullname, 'wb') as f:
                f.write(data)



def main() -> None:
    # get arguments from command line
    raw_arguments = docopt(__doc__, version=f'garmin-backup {__version__}')
    args = parse_arguments(raw_arguments)

    # Load environment variables if defined
    email = args['--username'] or os.getenv("USER")
    password = args['--password'] or os.getenv("PASSWORD")
    tokenstore = os.getenv("GARMINTOKENS") or TOKEN_STORE_DIR

    
    # initialise api
    if args['--fake']:
        api = FakeGarmin()
    else:
        api = init_api(email, password, tokenstore)

    # find activities to be downloaded
    os.makedirs(args['<path>'], exist_ok=True)
    activities_to_download = get_download_activities(args['<path>'], args['--start'], args['--end'], api)

    # download activities and save to disk
    download_activities(activities_to_download, args['--formats'])


if __name__ == '__main__':
    main()
