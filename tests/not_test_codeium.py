import pytest
from unittest.mock import patch, MagicMock
from src.garmin_backup import (
    init_api,
    download_activities,
    get_downloads_by_date,
    get_downloads_by_id,
    main,
)

# Fixtures
@pytest.fixture
def mock_garmin_api():
    with patch("garmin_backup.Garmin") as mock_garmin:
        yield mock_garmin

@pytest.fixture
def mock_activity_data():
    return [
        {"id": 1, "name": "Activity 1", "date": "2022-01-01"},
        {"id": 2, "name": "Activity 2", "date": "2022-01-02"},
    ]

# Unit Tests
def test_init_api_valid_credentials(mock_garmin_api):
    mock_garmin_api.return_value.login.return_value = True
    api = init_api("username", "password", "tokenstore")
    assert api is not None

def test_init_api_invalid_credentials(mock_garmin_api):
    mock_garmin_api.return_value.login.return_value = False
    with pytest.raises(GarminConnectAuthenticationError):
        init_api("username", "password", "tokenstore")

def test_download_activities_success(mock_garmin_api, mock_activity_data):
    mock_garmin_api.return_value.download_activity.return_value = b"activity_data"
    download_activities(mock_activity_data, ["GPX"], "/path/to/download", 1, mock_garmin_api)
    mock_garmin_api.return_value.download_activity.assert_called_once()

def test_download_activities_failure(mock_garmin_api, mock_activity_data):
    mock_garmin_api.return_value.download_activity.side_effect = Exception("Mock error")
    with pytest.raises(Exception):
        download_activities(mock_activity_data, ["GPX"], "/path/to/download", 1, mock_garmin_api)

def test_get_downloads_by_date(mock_activity_data):
    downloads = get_downloads_by_date(mock_activity_data, "2022-01-01", "2022-01-02")
    assert len(downloads) == 2

def test_get_downloads_by_id(mock_activity_data):
    downloads = get_downloads_by_id(mock_activity_data, [1, 2])
    assert len(downloads) == 2

# Integration Tests
def test_cli_options(tmpdir):
    # Create a test directory
    download_dir = tmpdir.mkdir("download")
    # Run the script with CLI options
    main(["--start", "2022-01-01", "--end", "2022-01-02", "--formats", "GPX", str(download_dir)])
    # Verify the correct activities are downloaded
    assert len(download_dir.listdir()) == 2

def test_activity_filtering(tmpdir):
    # Create a test directory with existing activity files
    download_dir = tmpdir.mkdir("download")
    existing_activity = download_dir.join("activity1.gpx")
    existing_activity.write("existing activity data")
    # Run the script to download new activities
    main(["--start", "2022-01-01", "--end", "2022-01-02", "--formats", "GPX", str(download_dir)])
    # Verify only new activities are downloaded
    assert len(download_dir.listdir()) == 3

def test_error_handling(tmpdir):
    # Run the script with an invalid API token
    with pytest.raises(GarminConnectAuthenticationError):
        main(["--start", "2022-01-01", "--end", "2022-01-02", "--formats", "GPX", str(tmpdir)])

# End-to-End Tests
def test_full_backup_scenario(tmpdir, mock_garmin_api):
    # Set up a test environment with a Garmin API account and some activities
    mock_garmin_api.return_value.get_activities.return_value = mock_activity_data
    # Run the script to download all activities
    main(["--start", "2022-01-01", "--end", "2022-01-02", "--formats", "GPX", str(tmpdir)])
    # Verify all activities are successfully downloaded and stored locally
    assert len(tmpdir.listdir()) == 2