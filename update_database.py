from google.cloud import bigquery
import datetime
from google.oauth2 import service_account
import os
from get_stock_data import get_stock_data

# Get yesterday's date
# date = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
date = "2025-04-25"
# Fetch stock data
data = get_stock_data(date=date)

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

if data:
    errors = client.insert_rows_json(table_id, data)
    if not errors:
        print("Data successfully inserted.")
    else:
        print(f"Errors occurred: {errors}")
else:
    print("No data to insert.")
