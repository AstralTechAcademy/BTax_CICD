import os
import requests
import pytest

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/sellAsset?key={API_KEY}"

def test_add_asset():
    resp = requests.post(URL, json={
        "origin" : {
            "wallet" : 88,
            "amount" : 16,
            "fiat" : 45,
            "eur_rate": 0.86
        },
        "destination" : {
            "wallet" : 74 ,
            "amount" : 192,
            "fiat" : 1.0
        },
        "fees": {
            "wallet" : 88,
            "amount": 0.0,
            "fiat": 1.0
        },
        "datetime" : "2026-06-16 17:19:16",
        "comments" : ""
    })
    print(resp)
    assert resp.status_code == 200

