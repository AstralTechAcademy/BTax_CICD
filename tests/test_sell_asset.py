import os
import requests
import json

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/sellAsset?key={API_KEY}"

def test_add_asset():
    expected_result= {"ops": [{"buy_price_eur": 31.0, "earnings": 38.500000000000014, "retired": 5.0, "sold_price_eur": 38.7}, {"buy_price_eur": 30.0, "earnings": 125.50000000000004, "retired": 10.0, "sold_price_eur": 38.7}, {"buy_price_eur": 28.38, "earnings": 135.82000000000005, "retired": 1.0, "sold_price_eur": 38.7}], "total_available": 25.0, "total_available_after": 9.0, "total_earnings": 135.82000000000005, "total_retired": 16.0}
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
    
    assert resp.status_code == 200
    assert resp.json() == expected_result

