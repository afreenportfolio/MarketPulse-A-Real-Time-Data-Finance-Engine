## Phase 2: Data Pipeline

1. I stored the daily stock data in a JSON file (with proper formatting to prevent formatting errors and increase human readability) to optimize API usage.
2. Developed a Python script that iterates through nested timeseries data to extract key metrics (**Open**, **High**, **Low**, **Close**, **Volume**)

### Features

- Read the local JSON file (`data.json`) to get the daily record as a dictionary and store it in `daily_records`.
- Convert all the keys (dates) into a list
- Loop through all the dates, and get the dictionary with all the key metrics, and print them.

### Setup Instructions:

1. Run the Python script and run it using `python real_time_market_pulse_dashboard_data_pipeline.py` to fetch the key metrics through the nested timeseries
2. Your data pipeline is ready!
