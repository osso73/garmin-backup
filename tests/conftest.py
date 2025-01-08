import pytest
import sys
from unittest.mock import patch


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


@pytest.fixture
def mock_activity_data():
    return [
        {"activityId": 1, "activityName": "Activity 1", "startTimeLocal": "2022-01-01T18:52:00.000Z"},
        {"activityId": 2, "activityName": "Activity 2", "startTimeLocal": "2022-01-02T09:36:00.000Z"},
    ]
    

@pytest.fixture
def mock_garmin_api():
    with patch("src.garmin_backup.Garmin") as mock_garmin:
        yield mock_garmin
