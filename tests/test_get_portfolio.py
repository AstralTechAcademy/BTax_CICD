import os
import requests
import json
import pytest

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

URL = f"https://{API_ENDPOINT}/getPortfolio"

def test_get_potfolio():
    res = requests.get(URL, params={"key": API_KEY})

    portfolio = json.loads(res.content)
    if not 'data' in portfolio.keys():
        assert False
    if not 'GIS' in portfolio['data']:
        assert False
    if not 'TEST5' in portfolio['data']:
        assert False
    
    asset_data = portfolio['data']['GIS']    
    assert asset_data['available'] == 25
    assert asset_data['dividendsEarned'] == 6
    assert asset_data['investedEur'] == 738.8
    assert asset_data['investedEurWithDividends'] == 732.8
    assert asset_data['priceAvgEur'] == 29.552
    assert asset_data['priceAvgEurWithDividends'] == 29.31

    asset_data = portfolio['data']['TEST5']    
    assert asset_data['available'] == 18
    assert asset_data['dividendsEarned'] == 0.0
    assert asset_data['investedEur'] == 818.7428
    assert asset_data['investedEurWithDividends'] == 818.74
    assert asset_data['priceAvgEur'] == 45.48571111
    assert asset_data['priceAvgEurWithDividends'] == 45.49

