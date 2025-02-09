import time
import requests
import json
from google.cloud import bigquery
from google.oauth2 import service_account
import os
from tickers_list import tickers
from data_validation.tickers_details_validation import TickerDetails


def get_ticker_details(tickers: list):
    url_base = "https://api.polygon.io/v3/reference/tickers/"
    headers = {
        "Authorization": "Bearer pLVCI0x7EyhQJRXh6SVB7rXmunyYH3Ki"
    }

    all_data = []
    request_count = 0

    for i, ticker in enumerate(tickers):
        url = f"{url_base}{ticker}"
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)["results"]
            all_data.append(data)
        else:
            print(f"Request for {ticker} failed with status code {response.status_code}")

        request_count += 1

        if request_count == 5:
            print("Waiting 60 seconds to stay within the API limit...")
            time.sleep(60)
            request_count = 0

        validated_data = [dict(TickerDetails(**element)) for element in all_data]

    return validated_data

tickers_details = get_ticker_details(tickers=tickers)


# BigQuery credentials and client setup
key_path = os.getenv("GOOGLE_CREDENTIALS_JSON")
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/bigquery"],
)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define BigQuery dataset and table
dataset_id = 'bionic-aspect-450214-c2.stock_data'
table_id = f'{dataset_id}.daily_data'


table = client.get_table(table_id)

if daily_data:
    errors = client.insert_rows_json(table_id, tickers_details)
    if not errors:
        print("Data successfully inserted.")
    else:
        print(f"Errors occurred: {errors}")
else:
    print("No data to insert.")
