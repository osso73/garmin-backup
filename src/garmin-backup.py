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
  --current                 Download activities for current year.
  -t, --type=TYPE           Get only activities of type TYPE. Possible values 
                            are [cycling, running, swimming,multi_sport, 
                            fitness_equipment, hiking, walking, other].
  -v, --verbose=LEVEL       Level of verbosity, from 1 to 3 [default: 1].
  --help                    Show this message and exit
  --version                 Show the version and exit.

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

The activities are saved on disk using the following name convention: 
`<ISO date>_HH.MM_<activity id>-<activity name>`.
"""

import datetime
import logging
import os

from getpass import getpass
import requests
from garth.exc import GarthHTTPError
from docopt import docopt

from garminconnect import Garmin, GarminConnectAuthenticationError


__version__ = '1.1'
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
    today = datetime.date.today()

    # if --current, override the start/end dates to match current year
    if args['--current']:
        args['--start'] = str(today.year)
        args['--end'] = None

    # dates parsing
    if args['--end']:
        args['--end'] = parse_date(args['--end'], date_type='end')
    else:
        args['--end'] = today  # latest date possible

    if args['--start']:
        args['--start'] = parse_date(args['--start'], date_type='start')
    else:
        args['--start'] = datetime.date(1900, 1, 1)  # just a very early date
    

    # format parsing
    args['--formats'] = args['--formats'].upper().split()
    for format in args['--formats']:
        if format not in ['ORIGINAL', 'GPX', 'CSV', 'TCX', 'KML']:
            raise Exception(
                "Invalid format. Type garmin-backup --help for more information"
            )

    # type parsing - ensure type is valid
    if args['--type']:
        if args['--type'] not in ['cycling', 'running', 'swimming', 
                'multi_sport', 'fitness_equipment', 'hiking, walking', 'other']:
            raise Exception(
                "Invalid type. Type garmin-backup --help for more information"
            )
    
    # activities parsing: transform to list
    if args['--activity']:
        args['--activity'] = args['--activity'].split()
        # args['--activity'] = [ int(act_id) for act_id in args['--activity']]
    
    # verbosity parsing: if wrong value, give it the default
    try:
        args['--verbose'] = int(args['--verbose'])
    except ValueError:
        args['--verbose'] = 1
    
    if args['--verbose'] not in [1, 2, 3]:
        args['--verbose'] = 1

    return args


def generate_activity_name(date: str, name:str, act_id:str) -> str:
    """return name of the activity file, built from the parameters"""
    start_time = datetime.datetime.fromisoformat(date)
    prefix = start_time.strftime("%Y-%m-%d_%H.%M")
    suffix = name.replace(' ', '_')
    return f'{prefix}_{act_id}-{suffix}'


def get_downloads_by_date(
    path: str, 
    start: datetime.date, 
    end: datetime.date, 
    type_a: str, 
    api: Garmin
) -> list[str]:
    """return list of activities (id, name) to be downloaded, by date"""

    # get activity names already in disk -- put in a set to remove duplicates
    files = os.listdir(path)
    disk_activities = {os.path.splitext(file)[0] for file in files}

    # get all activities available in garmin
    print("Getting the list of activities from the account...")
    garmin_activities = api.get_activities_by_date(start, end, type_a)
    garmin_activities = [
        {
            'name': generate_activity_name(a["startTimeLocal"], a["activityName"], a["activityId"]),
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

    activities_to_download = list()

    for act_id in list_of_ids:
        activity = api.get_activity_evaluation(act_id)
        activityName = activity['activityName']
        startTime = activity['summaryDTO']['startTimeLocal']
        activities_to_download.append(
            {
                'name': generate_activity_name(startTime, activityName, act_id),
                'id': act_id
            }
        )
    
    print(f"{len(activities_to_download)} activities to be downloaded.")
    print_separator()

    return activities_to_download


def print_progress_bar(
    iteration: int, total: int, prefix: str='', suffix: str='', length: int=30, fill: str='█'
) -> None:
    """Print progress bar for downloading activities"""

    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '·' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print('')  # adding a line return

def download_activities(
    activities: list[dict], formats: list[str], path: str, verbose: int, api:Garmin
) -> None:
    """
    download the activities from the list provided, and write
    files in disk. The list is a list of acitivities containing
    the 'id' and the 'name' for each activity.
    """

    total = len(activities)
    for i, activity in enumerate(activities):
        if verbose == 1:
            print_progress_bar(i+1, total, prefix='Progress:', suffix='Complete')
        else:
            print(f"Downloading activity {i+1} of {total}. Id: {activity['id']}")

        for file_format in formats:
            ext = 'zip' if file_format=="ORIGINAL" else file_format.lower()
            filename = f"{activity['name']}.{ext}"
            if verbose == 3:
                print(f'   Format {file_format}. Downloading {filename}...')

            dl_fmt = getattr(Garmin.ActivityDownloadFormat, file_format)
            data = api.download_activity(activity['id'], dl_fmt=dl_fmt)
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
            args['<path>'], args['--start'], args['--end'], args['--type'], api
        )

    # download activities and save to disk
    download_activities(
        activities_to_download, 
        args['--formats'], 
        args['<path>'], 
        args['--verbose'], 
        api
    )
    
    # separator  from downloaded activities (only if downloaded >0 activities)
    if len(activities_to_download): 
        print_separator()
    
    # final message -- copied from Garmin Connect example :)
    print("\nDone. Be active, generate some data to fetch next time ;-) Bye!")


if __name__ == '__main__':
    main()
