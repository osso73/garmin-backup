import pytest
from unittest.mock import patch


import src.garmin_backup as gb


class TestPrintSeparator:
    def test_print_separator(self, capture_stdout):
        gb.print_separator()
        expected = '-' * 50 + "\n"
        assert capture_stdout['stdout'] == expected


class TestGetCredentials:

    @pytest.mark.parametrize("name, pwd", [
        ["john", "secret123"],
        ["user", "password00"],
    ])
    def test_get_credentials(self, name, pwd):
        with patch('builtins.input', return_value=name):
            with patch('src.garmin_backup.getpass', return_value=pwd):
                user, password = gb.get_credentials()
                assert user == name
                assert password == pwd


class TestInitApi:
    def test_init_api_valid_credentials(self, mock_garmin_api):
        mock_garmin_api.return_value.login.return_value = True
        api = gb.init_api("username", "password", "tokenstore")
        assert api is not None
    
    @pytest.mark.skip(reason="not yet implemented")
    def test_init_api_invalid_credentials(self, mock_garmin_api):
        mock_garmin_api.return_value.login.return_value = False
        with pytest.raises(gb.GarminConnectAuthenticationError):
            gb.init_api("username", "password", "tokenstore")
    
    @pytest.mark.skip(reason="not yet implemented")
    def test_init_api_invalid_tokenstore(self, mock_garmin_api):
        with pytest.raises(FileNotFoundError):
            gb.init_api("username", "password", "tokenstore")
    
    @pytest.mark.skip(reason="not yet implemented")
    def test_init_api_no_credentials(self, mock_garmin_api):
        with pytest.raises(gb.GarminConnectAuthenticationError):
            gb.init_api(None, None, None)
    
    @pytest.mark.skip(reason="not yet implemented")
    def test_init_api_no_tokenstore(self, mock_garmin_api):
        with pytest.raises(FileNotFoundError):
            gb.init_api("username", "password", None)
    
    @pytest.mark.skip(reason="not yet implemented")
    def test_init_api_no_credentials_or_tokenstore(self, mock_garmin_api):
        with pytest.raises(gb.GarminConnectAuthenticationError):
            gb.init_api(None, None, None)


class TestGenerateActivityName:

    @pytest.mark.parametrize("date, name, act_id, result", [
        ["2024-12-17T17:52", "Salida en bici", "id003123", "2024-12-17_17.52_id003123-Salida_en_bici"],
        ["1973-06-24T09:38", "Natación en piscina", "id34", "1973-06-24_09.38_id34-Natación_en_piscina"],
    ])
    def test_generate_activity_name(self, date, name, act_id, result):
        name_generated = gb.generate_activity_name(date, name, act_id)
        assert name_generated == result
    


class TestGetDownloadsByDate:
    def test_get_downloads_by_date(self, mock_activity_data, capture_stdout):
        with patch('src.garmin_backup.api.get_activities_by_date', return_value=mock_activity_data):
            downloads = gb.get_downloads_by_date(
                'TBC', '2022-01-01', '2022-01-02', 'GPX', 'TBC'
            )

        assert len(downloads) == 2
        assert downloads[0] == {"id": 1, "name": "Activity 1", "date": "2022-01-01"}
        assert downloads[1] == {"id": 2, "name": "Activity 2", "date": "2022-01-02"}
