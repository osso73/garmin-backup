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
  --help                    Show this message and exit.
  --verion                  Show the version and exit.

The username and password can also be provided through environment variables 
USER and PASSWORD. If not provided through command line or environment 
variables, the program will prompt for this information the first time. The 
credential information will then be stored in .garminconnect folder under user
profile, and re-used for the future, until they need to be refreshed.

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


__version__ = '0.7'
TOKEN_STORE_DIR = "~/.garminconnect"
MAX_ACTIVITIES = 100

# Configure debug logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def print_separator():
    """print line in terminal, to separate sections"""
    print('-' * 50)


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
        return datetime.date.fromisoformat(date)


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
            raise Exception(
                "Invalid format. Type garmin-backup --help for more information"
            )
    
    # activities parsing: transform to list of int
    if args['--activity']:
        args['--activity'] = args['--activity'].split()
        args['--activity'] = [ int(act_id) for act_id in args['--activity']]

    return args


def generate_activity_name(date: str, name:str) -> str:
    """return name of the activity file, built from the parameters"""
    start_time = datetime.datetime.fromisoformat(date)
    prefix = start_time.strftime("%Y-%m-%d_%H%M")
    suffix = name.replace(' ', '_')
    return f'{prefix}-{suffix}'


def get_downloads_by_date(
    path: str, start: datetime.date, end: datetime.date, api: Garmin
) -> list[str]:
    """return list of activities (id, name) to be downloaded, by date"""

    # get activity names already in disk -- put in a set to remove duplicates
    files = os.listdir(path)
    disk_activities = {file.split('.')[0] for file in files}

    # get all activities available in garmin
    print("Getting the list of activities from the account...")
    garmin_activities = api.get_activities_by_date(start, end)
    garmin_activities = [
        {
            'name': generate_activity_name(a["startTimeLocal"], a["activityName"]),
            'id': a["activityId"]
        }
        for a in garmin_activities
    ]
    print(f"Found {len(garmin_activities)} activities between {start} and {end}.")

    # download activities are those that are not in disk already
    download_activities = [
        activity
        for activity in garmin_activities
        if activity['name'] not in disk_activities
    ]
    print(f"{len(download_activities)} activities are not in local disk.")

    # trunkate list if it exceeds the maximum allowed
    if len(download_activities) > MAX_ACTIVITIES:
        download_activities = download_activities[:MAX_ACTIVITIES]
        
    print(f"{len(download_activities)} activities to be downloaded.")
    print_separator()

    return download_activities


def get_downloads_by_id(list_of_ids, api):
    """return list of activities (id, name) to be downloaded, by ids"""

    print(f"Got {len(list_of_ids)} activities.")

    download_activities = list()

    for act_id in list_of_ids:
        activity = api.get_activity_evaluation(act_id)
        activityName = activity['activityName']
        startTime = activity['summaryDTO']['startTimeLocal']
        download_activities.append(
            {
                'name': generate_activity_name(startTime, activityName),
                'id': act_id
            }
        )
    
    print(f"{len(download_activities)} activities to be downloaded.")
    print_separator()

    return download_activities


def download_activities(
    activities: list[dict], formats: list[str], path: str, api:Garmin
) -> None:
    """
    download the activities from the list provided, and write
    files in disk. The list is a list of acitivities containing
    the 'id' and the 'name' for each activity.
    """

    total = len(activities)
    for i, activity in enumerate(activities):
        print(f"Downloading activity {i+1} of {total}. Id: {activity['id']}")

        for file_format in formats:
            ext = 'zip' if file_format=="original" else file_format
            filename = f"{activity['name']}.{ext}"
            print(f'   Format {file_format}. Downloading {filename}...')
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
            fullname = os.path.join(path, filename)
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
    print_separator()
    print('Connecting to Garmin Connect...')

    api = init_api(email, password, tokenstore)

    print('Connection established for user:', api.get_full_name())
    print_separator()

    # find activities to be downloaded
    os.makedirs(args['<path>'], exist_ok=True)
    if args['--activity']:
        activities_to_download = get_downloads_by_id(args['--activity'], api)
    else:
        activities_to_download = get_downloads_by_date(
            args['<path>'], args['--start'], args['--end'], api
        )

    # download activities and save to disk
    download_activities(
        activities_to_download, 
        args['--formats'], 
        args['<path>'], 
        api
    )
    
    # separator  from downloaded activities (only if downloaded >0 activities)
    if len(activities_to_download): 
        print_separator()
    
    # final message -- copied from Garmin Connect example :)
    print("\nDone. Be active, generate some data to fetch next time ;-) Bye!")


if __name__ == '__main__':
    main()
