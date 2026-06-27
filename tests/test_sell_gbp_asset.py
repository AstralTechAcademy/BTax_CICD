import os
import requests
import json

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/sellAsset?key={API_KEY}"

def test_sell_gbp_asset():
    expected_result= {"ops": [{"buy_price_eur": 27.43, "earnings": 22.540000000000006, "retired": 2.0, "sold_price_eur": 38.7}], "total_available": 5.0, "total_available_after": 3.0, "total_earnings": 22.540000000000006, "total_retired": 2.0}
    resp = requests.post(URL, params={"cicd": 1}, json={
        "origin" : {
            "wallet" : 90,
            "amount" : 2,
            "fiat" : 45,
            "eur_rate": 0.86
        },
        "destination" : {
            "wallet" : 92,
            "amount" : 77.4,
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

