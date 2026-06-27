import os
import requests
import json

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/sellAsset?key={API_KEY}"

def test_sell_usd_asset():
    expected_result= {"ops": [{"buy_price_eur": 31.67, "earnings": 37.169999999999966, "retired": 7.0, "sold_price_eur": 36.98}, {"buy_price_eur": 31.373999999999995, "earnings": 42.77599999999997, "retired": 1.0, "sold_price_eur": 36.98}], "total_available": 13.0, "total_available_after": 5.0, "total_earnings": 42.77599999999997, "total_retired": 8.0}
    resp = requests.post(URL, params={"cicd": 1}, json={
        "origin" : {
            "wallet" : 91,
            "amount" : 8,
            "fiat" : 43,
            "eur_rate": 0.86
        },
        "destination" : {
            "wallet" : 92,
            "amount" : 295.84,
            "eur_rate" : 1.0
        },
        "fees": {
            "wallet" : 92,
            "amount": 0.0,
            "eur_rate": 1.0
        },
        "datetime" : "2026-06-16 17:19:16",
        "comments" : ""
    })
    
    assert resp.status_code == 200
    assert resp.json() == expected_result

