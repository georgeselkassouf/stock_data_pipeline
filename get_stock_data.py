import requests
import json
import os
from data_validation.stock_data_validation import StockData
from tickers_list import tickers

token = os.getenv("API_KEY")

def get_stock_data(date: str):

    url = f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{date}?adjusted=true"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url=url, headers=headers)

    # Check if the status code is 200
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
        
    response_data = json.loads(response.text)

    if response_data.get("resultsCount", 0) <= 0:
        print("No results found.")
        return []
    else:
        data = response_data["results"]
        filtered_data = [element for element in data if element.get("T", "") in tickers]

    validated_data = [dict(StockData(**element)) for element in filtered_data]

    return validated_data
