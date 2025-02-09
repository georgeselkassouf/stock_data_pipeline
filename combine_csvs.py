import os
import pandas as pd

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
        df['Ticker'] = file.split('.')[0]

        # Convert the dataframe to a list of dictionaries and append to the combined_data list
        combined_data.extend(df.to_dict(orient='records'))

    return combined_data


combined_stock_data=combine_csvs(folder_path='historical_data')
