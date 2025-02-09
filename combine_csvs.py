import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from data_validation.historical_data_valdiation import historical_data_validation

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
        df['ticker'] = file.split('.')[0]

        # Convert the date column to datetime and append '00:00:00' as the time part
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d') + ' 00:00:00'

        # Convert the dataframe to a list of dictionaries and append to the combined_data list
        combined_data.extend(df.to_dict(orient='records'))

        validated_data = [dict(HistoricalData(**element)) for element in combined_data]

    return validated_data


combined_stock_data=combine_csvs(folder_path='historical_data')


# BigQuery credentials and client setup
key_path = os.getenv("GOOGLE_CREDENTIALS_JSON")
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/bigquery"],
)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define BigQuery dataset and table
dataset_id = 'bionic-aspect-450214-c2.stock_data'
table_id = f'{dataset_id}.data'


table = client.get_table(table_id)

if combined_stock_data:
    errors = client.insert_rows_json(table_id, combined_stock_data)
    if not errors:
        print("Data successfully inserted.")
    else:
        print(f"Errors occurred: {errors}")
else:
    print("No data to insert.")
