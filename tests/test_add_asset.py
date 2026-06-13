import os
import requests
import pytest

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/assets?key={API_KEY}"

def test_add_asset():
    resp = requests.post(URL, json={
        "name": "TEST1",
        "type": "share",
        "country": 2,
        "currency": 1
    })
    assert resp.status_code == 200

