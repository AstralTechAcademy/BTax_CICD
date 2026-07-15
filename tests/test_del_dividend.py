import os
import requests
import json
import pytest

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/dividends"

def test_del_dividend():
    res = requests.get(URL, params={"key": API_KEY, "asset": "TEST2"})

    dividends = json.loads(res.content)
    for d in dividends:
        resp = requests.delete(URL, params={"key": API_KEY, "id": d['id']})
        assert resp.status_code == 200
    assert True

