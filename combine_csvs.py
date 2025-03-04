import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from data_validation.historical_data_validation import HistoricalData
import math
from datetime import datetime

def combine_csvs(folder_path):
    # List of all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # List to store all rows as dictionaries
    combined_data = []

    # Loop through all CSV files and process them
    for file in csv_files:
        # Read the CSV file into a dataframe
        df = pd.read_csv(os.path.join(folder_path, file))

        # Add a new column 'Ticker' with the name of the file (without extension)
        df['ticker'] = file.rsplit('.csv', 1)[0]

        # Convert 'date' field to '%Y-%m-%d %H:%M:%S'
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d %H:%M:%S')

        # Convert the dataframe to a list of dictionaries and append to the combined_data list
        combined_data.extend(df.to_dict(orient='records'))

    validated_data = [dict(HistoricalData(**element)) for element in combined_data]

    return validated_data


def insert_data_in_batches(client, table_id, combined_stock_data, batch_size=5000):
    """Insert data into BigQuery in smaller batches to avoid errors."""
    # Calculate the number of batches needed
    num_batches = math.ceil(len(combined_stock_data) / batch_size)

    for i in range(num_batches):
        batch_data = combined_stock_data[i * batch_size: (i + 1) * batch_size]
        errors = client.insert_rows_json(table_id, batch_data)
        if errors:
            print(f"Error in batch {i + 1}: {errors}")
        else:
            print(f"Batch {i + 1} successfully inserted.")


# Combine data from CSVs
combined_stock_data = combine_csvs(folder_path='historical_data')

# BigQuery credentials and client setup
key_path = os.getenv("GOOGLE_CREDENTIALS_JSON")
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/bigquery"],
)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define BigQuery dataset and table
dataset_id = 'bionic-aspect-450214-c2.stock_data'
table_id = f'{dataset_id}.historical_data'

# Insert data into BigQuery in batches
if combined_stock_data:
    insert_data_in_batches(client, table_id, combined_stock_data, batch_size=10000)
else:
    print("No data to insert.")
