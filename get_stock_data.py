import requests
import json
from data_validation import StockData
import os


token = os.getenv("API_KEY")

tickers = [
    'AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'META', 'TSLA', 'ASML', 'ORCL', 'COST', 'CSCO',
    'MCD', 'DHR', 'NKE', 'ADBE', 'TMO', 'DIS', 'NFLX', 'INTC', 'LIN', 'AMD', 'HON', 'AMGN','LOW', 'MDT'
]

def get_stock_data(date: str):

    url = f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{date}?adjusted=true"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200 and json.loads(response.text)["resultsCount"] > 0:

        data = json.loads(response.text)["results"]

        filtered_data = [
            element for element in data if element.get("T", "") in tickers
        ]

        validated_data = [dict(StockData(**element)) for element in filtered_data]
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    return validated_data
