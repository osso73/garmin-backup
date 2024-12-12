# garmin-backup changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). For the version numbers, I just use a simple 2-digit, for major and minor changes. I add a letter in the case I create a new version fixing only bugs.

Each version has its corresponding apk under the folder `releases`.


## v2.0 -  2024-11-10

Changed command line parser to click. This results in some changes in the way parameters are provided in the command line, therefore requiring a major versio change.

, such as for multiple choice options, we need to enter the option several times instead of having a list. Example, for multiple formats we now need to enter:

- Now: `garmin-backup -f CSV -f GPX`
- Before: `garmin-backup -f "csv gpx"`


### Changed
- For multiple choice options, now it is required to enter the option several times instead of having a list in "". This applies to `formats` and `activities`.
- Format choices are now required in uppercase


## v1.1 - 2024-03-15

Include activity id in the name of the downloaded file.


### Changed
- Name of the files downloaded, to include activity id.


### Added
- `cx_freeze` configuration, to create a packaged version for windows.


## v1.0 - 2024-03-13

Finalise the main options I wanted to implement, and moving to the first 1.0 version.


### Added
- Option to define verbosity (iss. #1)


## v0.8 - 2024-03-09

### Added
- Option to download activity by id (iss. #2)
- Option to download current year (iss. #3)
- Option to filter activities by type (iss. #5)
