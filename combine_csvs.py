import os
import pandas as pd


def combine_csvs(folder_path):

    # List of all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # List to store all dataframes
    dfs = []

    # Loop through all CSV files and process them
    for file in csv_files:
        # Read the CSV file into a dataframe
        df = pd.read_csv(os.path.join(folder_path, file))

        # Add a new column 'ticker' with the name of the file (without extension)
        df['Ticker'] = file.split('.')[0]

        # Append the dataframe to the list
        dfs.append(df)

    # Concatenate all the dataframes into one
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save the combined dataframe to a new CSV file
    combined_df.to_csv('combined_stock_data.csv', index=False)

    print("All files have been successfully combined into 'combined_stock_data.csv'.")


combined_stock_data=combine_csvs(folder_path='historical_data')
