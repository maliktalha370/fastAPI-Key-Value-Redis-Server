import pytest
import requests

BASE_URL = 'http://localhost:8000'

@pytest.mark.parametrize("key, expected_status_code", [
    ("9a14cfc9-a3d1-4b14-a0cd-a1c6785fbaab", 200),
    ("non_existing_key", 404),
])
def test_get_value(key, expected_status_code):
    response = requests.get(f"{BASE_URL}/get/{key}")
    assert response.status_code == expected_status_code
    if response.status_code == 200:
        assert response.text
