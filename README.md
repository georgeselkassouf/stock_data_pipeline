# Stock Data Pipeline

This project fetches daily stock data from an external API, processes it, and updates a Google BigQuery table. The pipeline is automated and runs daily at **11:30 PM UTC+2** using GitHub Actions.

## Features

- **Fetch stock data**: Retrieves stock data for a specified date using the Polygon API.
- **Update Google BigQuery**: Inserts the fetched stock data into a BigQuery table.
- **Automated execution**: The pipeline runs daily at midnight UTC+2 using GitHub Actions.
- **Google Cloud Integration**: Uses service account credentials stored securely in GitHub Secrets for authentication.

## GitHub Actions

This project uses GitHub Actions to automate the daily execution of the pipeline:

### Workflow

- **Trigger**: The workflow runs daily at 12:00 AM UTC+2 (10:00 PM UTC).
- **Jobs**: 
  - **Checkout the repository**: Ensures the latest code is pulled.
  - **Set up Python**: Configures the required Python version (3.9 in this case).
  - **Install dependencies**: Installs all the required Python packages.
  - **Authenticate with Google Cloud**: Uses the base64-encoded service account credentials stored as a GitHub secret.
  - **Run update_database.py**: Executes the script to update the database with the latest stock data.
