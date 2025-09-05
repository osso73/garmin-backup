#!/usr/bin/env python3

"""
gamin-backup is a script to download your activities from 
Garmin Connect, so you can keep a local copy in your computer.
"""

import datetime
import logging
import os

from getpass import getpass
import requests
from garth.exc import GarthHTTPError
import click

from garminconnect import Garmin, GarminConnectAuthenticationError


__version__ = '2.0'
TOKEN_STORE_DIR = "~/.garminconnect"
MAX_ACTIVITIES = 100

# Configure debug logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def print_separator() -> None:
    """print line in terminal, to separate sections"""
    print('-' * 50)


def get_credentials() -> tuple[str, str]:
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


def generate_activity_name(date: str, name:str, act_id:str) -> str:
    """return name of the activity file, built from the parameters"""
    start_time = datetime.datetime.fromisoformat(date)
    prefix = start_time.strftime("%Y-%m-%d_%H.%M")
    suffix = sanitize(name.replace(' ', '_'))
    return f'{prefix}_{act_id}-{suffix}'


def sanitize (filename: str) -> str:
    """
    return sanitized name of the activity file, built from the parameters
    Simplified version of the sanitize function from sanitize-filename
    """
    blacklist = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|", "\0"]
    modified = "".join(c for c in filename if c not in blacklist)

    return modified

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
            'name': generate_activity_name(
                a["startTimeLocal"],
                a.get("activityName", "Untitled"), # some activities have no name
                a["activityId"]
            ),
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


def get_downloads_by_id(list_of_ids: tuple[str], api: Garmin) -> list[str]:
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
    activities: list[dict], formats: list[str], path: str, verbose: int, api: Garmin
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


class DateOrYear(click.ParamType):
    """Custom parameter type for date or year"""
    name = "date_or_year"

    def __init__(self, is_start_date=True):
        self.is_start_date = is_start_date

    def convert(self, value, param, ctx):
        # If value is already a datetime.date, return it as-is (no conversion needed
        if isinstance(value, datetime.date):
            return value
        try:
            # Try parsing as full ISO date
            return datetime.date.fromisoformat(value)
        except ValueError:
            try:
                # Try parsing as just a year
                year = int(value)
                if 1000 <= year <= 9999:  # Adjust year range as needed
                    if self.is_start_date:
                        return datetime.date(year, 1, 1)  # January 1st for start date
                    else:
                        return datetime.date(year, 12, 31)  # December 31st for end date
                else:
                    self.fail(f"Year {year} is out of range", param, ctx)
            except ValueError:
                self.fail(f"{value} is not a valid ISO date or year", param, ctx)

@click.command(epilog="""
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
""")
@click.argument("path", type=click.Path())
@click.option('-f', '--formats', 
    default=['GPX'], 
    type=click.Choice(['ORIGINAL', 'GPX', 'CSV', 'TCX', 'KML']), 
    multiple=True, 
    help='Which formats to download [default: GPX]. For more than one type, \
you can enter the option several times.'
    )
@click.option('-u', '--username', 
    help='Username of your Garmin account. Can also be passed as USER \
environment variable.'
    )
@click.option('-p', '--password', 
    help='Password of your Garmin account. Can also be passed as PASSWORD \
environment variable.'
    )
@click.option('-a', '--activity', 
    multiple=True, 
    help='Activity ID. Download only that activity, even if it has already \
been downloaded. Can be entered multiple times.'
    )
@click.option('-s', '--start', 
    type=DateOrYear(is_start_date=True), 
    default=datetime.date(1900, 1, 1), 
    help='Start date, in ISO format. If only the year is provided, it will \
assume Jan 1st of that year.'
    )
@click.option('-e', '--end', 
    type=DateOrYear(is_start_date=False), 
    default=datetime.date.today(), 
    help='End date, in ISO format. If only the year is provided, it will \
assume Dec 31st of that year.'
    )
@click.option('--current', 
    is_flag=True, 
    help='Download activities for current year.'
    )
@click.option('-t', '--act_type', 
    type=click.Choice(['cycling', 'running', 'swimming', 'multi_sport', 
                    'fitness_equipment', 'hiking', 'walking', 'other']), 
    multiple=True, help='Get only activities of type TYPE.'
    )
@click.option('-v', '--verbose', 
    type=click.IntRange(1, 3), 
    default=1, 
    help='Level of verbosity.'
    )
@click.version_option(version=__version__)
def main(**kwargs) -> None:
    """
    gamin-backup is a script to download your activities from 
    Garmin Connect, so you can keep a local copy in your computer.

    It will download the activities on the PATH provided.
    """
    # if --current, override the start/end dates to match current year
    if kwargs['current']:
        today = datetime.date.today()
        kwargs['start'] = datetime.date(today.year, 1, 1)
        kwargs['end'] = today

    # Load environment variables if defined
    email = kwargs['username'] or os.getenv("USER")
    password = kwargs['password'] or os.getenv("PASSWORD")
    tokenstore = os.getenv("GARMINTOKENS") or TOKEN_STORE_DIR
    
    # initialise api
    print_separator()
    print('Connecting to Garmin Connect...')

    api = init_api(email, password, tokenstore)

    print('Connection established for user:', api.get_full_name())
    print_separator()

    # find activities to be downloaded
    os.makedirs(kwargs['path'], exist_ok=True)
    if kwargs['activity']:
        activities_to_download = get_downloads_by_id(kwargs['activity'], api)
    else:
        activities_to_download = get_downloads_by_date(
            kwargs['path'], kwargs['start'], kwargs['end'], kwargs['act_type'], api
        )

    # download activities and save to disk
    download_activities(
        activities_to_download, 
        kwargs['formats'], 
        kwargs['path'], 
        kwargs['verbose'], 
        api
    )
    
    # separator  from downloaded activities (only if downloaded >0 activities)
    if len(activities_to_download): 
        print_separator()
    
    # final message -- copied from Garmin Connect example :)
    print("\nDone. Be active, generate some data to fetch next time ;-) Bye!")


if __name__ == '__main__':
    main()
