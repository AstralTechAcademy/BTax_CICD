import os
import requests
import json
import pytest
from datetime import datetime, timedelta

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/prices"

def test_get_stock_prives():
    res = requests.get(URL, params={"key": API_KEY})
    price_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")

    assert res.status_code == 200

    prices = json.loads(res.content)['data']
    assert len(prices) > 0
    assert prices[0]['price_date'] == price_date

