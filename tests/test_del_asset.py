import os
import requests
import pytest

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/assets"

def test_del_asset():
    resp = requests.delete(URL, params={"key": API_KEY, "name": "TEST1"})
    assert resp.status_code == 200

