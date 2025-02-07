import requests
import json
from data_validation import StockData


def get_stock_data(date: str):

    token = os.getenv("API_KEY")

    url = f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{date}?adjusted=true"

    headers = {
    "Authorization": f"Bearer {token}"
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200 and json.loads(response.text)["resultsCount"] > 0:

        data = json.loads(response.text)["results"]

        validated_data = [dict(StockData(**element)) for element in data]

    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    return validated_data
