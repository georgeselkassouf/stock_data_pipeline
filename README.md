# Stock Data Processing Workflow

This repository automates the process of combining stock data, retrieving ticker details, and updating a database using GitHub Actions. The workflow is triggered both manually and on a scheduled basis.

## Overview

The GitHub Actions workflow automates three core tasks:

1. **Combine CSV Files**: Merges multiple stock data CSV files into one consolidated file.
2. **Fetch Ticker Details**: Retrieves detailed information about stock tickers.
3. **Update Database**: Updates the database with the previous day's stock data.

### Workflow Trigger
- **Scheduled Cron Job**: Runs from Tuesday to Saturday at **22:00 PM UTC+2** (20:00 PM UTC).
- **Manual Trigger**: You can also manually trigger the workflow via GitHub UI.

> ⏳ **Execution Period**: The workflow ran from **March 4th to April 12th**, retrieving stock data for the previous day each time. As a result, data was collected from **March 3rd to April 11th**.

## Prerequisites

Before running the workflow, ensure the following:

1. **Secrets**:
   - `GOOGLE_CREDENTIALS_JSON`: Base64 encoded Google Cloud service account credentials.
   - `API_KEY`: API key required by the scripts to fetch stock data.

2. **requirements.txt**: Ensure you have a `requirements.txt` file that lists the necessary Python dependencies for the scripts.

3. **Python 3.9**: The workflow is set to use Python version 3.9. Make sure your environment is compatible.

## Workflow Details

### Jobs in the Workflow

#### 1. **Combine CSVs Job**
- **Purpose**: Combines multiple CSV files into one consolidated CSV file.
- **Steps**:
  1. Check out the repository.
  2. Set up Python and install dependencies.
  3. Authenticate with Google Cloud.
  4. Check for the existence of a marker file to avoid re-running.
  5. If no marker file exists, run `combine_csvs.py`.
  6. Commit a marker file indicating the job is complete.

#### 2. **Get Ticker Details Job**
- **Purpose**: Retrieves detailed information for various stock tickers.
- **Steps**:
  1. Check out the repository.
  2. Set up Python and install dependencies.
  3. Authenticate with Google Cloud.
  4. Check for the existence of a marker file to avoid re-running.
  5. If no marker file exists, run `get_ticker_details.py`.
  6. Commit a marker file indicating the job is complete.

#### 3. **Update Database Job**
- **Purpose**: Updates the database with the latest stock data.
- **Steps**:
  1. Check out the repository.
  2. Set up Python and install dependencies.
  3. Authenticate with Google Cloud.
  4. Run the `update_database.py` script to update the database.

---

## 📊 Power BI Dashboard

You can explore the resulting stock data in the interactive Power BI dashboard here:

🔗 [View Dashboard](https://app.powerbi.com/view?r=eyJrIjoiY2JmOGU4ODgtMDRlNS00ZDgwLTk5ZTItMjhiNTViODE0NDM0IiwidCI6ImRkZjhiYWQyLWY4ZGEtNDg3Zi05OGQ1LWQzMGExNjM0MjA0OSJ9)

---

## Cloning the Repository

To clone this repository to your local machine, follow these steps:

1. **Install Git**: If you haven't already, make sure Git is installed on your system. You can download and install it from [here](https://git-scm.com/downloads).

2. **Clone the Repository**:
   - Open your terminal (or Git Bash on Windows).
   - Navigate to the directory where you want to clone the repository.
   - Run the following command:

   ```bash
   git clone https://github.com/georgeselkassouf/stock_data_pipeline.git
