# garmin-backup

Script to backup your activities from Garmin to the local disk. It uses the API from [GarminConnect](https://github.com/cyberjunky/python-garminconnect) to authenticate, store the session credentials, and download data from Garmin site. 


**Why create this script?**

I am implementing a functionality similar to other available tools, such as [garminexport](https://github.com/petergardfjall/garminexport) or [garpy](https://github.com/felipeam86/garpy), both of which I have been using until Garmin Connect changed the authentication method and these scripts have stopped working. This is why I have implemented ``garmin-backup``, using the [GarminConnect](https://github.com/cyberjunky/python-garminconnect) API that works now. Besides that, I've added a functionality that I missed from the other two scripts: the limitation on dates. This allows me to store my data in different folders per year, rather than having all activities in a single folder, which as becoming a bit too many over the years.

Note this is just using a very limited subset of GarminConnect, only focused at downloading the activity data for now. Maybe later other functions will be added, but I'm not really interested in extracting other data.



## Installation

Just clone or download the repository, create a virtual environment with the requirements, and that's it. You need to have python installed in your environment.

```bash
git clone https://github.com/osso73/garmin-backup.git
cd garmin-backup
python -m venv .venv
.venv/Scripts/activate.bat   # for linux use: source .venv/bin/activate
pip install -r requirements.txt
```

That's it, you can run the program in `src/garmin-backup`:

```bash
cd src
python garmin-backup data  # see the usage below for all the available options
```



## Usage

    Usage: garmin-backup.py [OPTIONS] PATH

    gamin-backup is a script to download your activities from  Garmin Connect,
    so you can keep a local copy in your computer.

    It will download the activities on the PATH provided.

    Options:
    -f, --formats [ORIGINAL|GPX|CSV|TCX|KML]
                                    Which formats to download [default: GPX].
                                    For more than one type, you can enter the
                                    option several times.
    -u, --username TEXT             Username of your Garmin account. Can also be
                                    passed as USER environment variable.
    -p, --password TEXT             Password of your Garmin account. Can also be
                                    passed as PASSWORD environment variable.
    -a, --activity TEXT             Activity ID. Download only that activity,
                                    even if it has already been downloaded. Can
                                    be entered multiple times.
    -s, --start DATE_OR_YEAR        Start date, in ISO format. If only the year
                                    is provided, it will assume Jan 1st of that
                                    year.
    -e, --end DATE_OR_YEAR          End date, in ISO format. If only the year is
                                    provided, it will assume Dec 31st of that
                                    year.
    --current                       Download activities for current year.
    -t, --act_type [cycling|running|swimming|multi_sport|fitness_equipment|hiking|walking|other]
                                    Get only activities of type TYPE.
    -v, --verbose INTEGER RANGE     Level of verbosity.  [1<=x<=3]
    --version                       Show the version and exit.
    --help                          Show this message and exit.

    The username and password can also be provided through environment variables
    USER and PASSWORD. If not provided through command line or environment
    variables, the program will prompt for this information the first time. The
    credential information will then be stored in .garminconnect folder under
    user profile, and re-used for the future, until they need to be refreshed.

    All activities between S_DATE and E_DATE that are not already present in
    <path>  will be downloaded. If no dates are provided, it will assume all
    activities,  from the beginning until today.

    There is a limit of 100 activities at a time, in order to avoid overloading
    the Garmin Connect page, and getting banned. If you have more than 100
    activities to download, you can just run the program again.

    The activities are saved on disk using the following name convention:  `<ISO
    date>_HH.MM_<activity id>-<activity name>`.



Examples:
```bash
# download all activities from 2020 to now, format gpx, save to folder ./data
garmin-backup data -s 2020

# download activities for current year, format csv and original
garmin-backup data/2024 --current -f CSV -f ORIGINAL

# download all activities for year 2023, in gpx
garmin-backup data/2023 -s 2023 -e 2023

# download activities for month of July 2023, in gpx and original
garmin-backup data/2023/07 -s=2023-07-01 -e=2023-07-31 -f GPX -f ORIGINAL
```


## License

This project is using an MIT license.
