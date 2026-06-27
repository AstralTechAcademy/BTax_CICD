import os
import requests
import pytest

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/dividends?key={API_KEY}"

def test_add_dividend():
    resp = requests.post(URL, json={
    "op_type":"dividend",
    "wallets":{"origin":{"id":90,"assetName":"TEST2","currency":"USD","exchange":"interactive"},
    "destination":{"id":0,"assetName":"EUR","currency":"EUR","exchange":"interactive"}},
    "details":{
        "assetName":"TEST2",
        "exchange":"interactive",
        "destination_net_amount":10.0,
        "destination_currency":"EUR",
        "is_tax_destination_paid":False,
        "destination_taxes":2.0,
        "destination_gross_amount":10,
        "origin_net_amount":11.62,
        "origin_taxes_paid":1.0,
        "origin_gross_amount":12.62,
        "origin_currency":"USD",
        "currency_rate":0.86,
        "destination_currency_rate":1.0,
        "date":"2025-07-05 01:09:14",
        "dividend_type":"dividend"
        }
    })
    assert resp.status_code == 200

