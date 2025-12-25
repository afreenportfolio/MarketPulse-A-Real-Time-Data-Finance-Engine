# MarketPulse-A-Real-Time-Data-Finance-Engine
MarketPulse: An end-to-end data engineering project featuring a robust Python pipeline, local JSON caching for API optimization, and a SQL-backed historical data warehouse.

## Phase 1: Data Pipeline
1.	I developed a Python script to fetch daily stock data (IBM) via Alpha Vantage API.
2.	I stored the daily stock data in a JSON file (with proper formatting to prevent formatting errors) to optimize API usage.
3.	Developed a Python script that iterates through nested timeseries data to extract key metrics (Open, High, Low, Close)

### Challenge:
⦁	Initial raw data from Python IDLE used single quotes (''), which caused json.decode errors as the standard JSON format requires double quotes ("").
⦁	This was fixed by implementing a manual data sanitation step (and exploring automated string replacement) to ensure the local storage strictly follows JSON standards and seamlessly parses with Python's json library

### Setup Instructions:
1.	Navigate to the Alpha Vantage Support Page
2.	Sign up (it's free!)
3.	Save the API key you get securely.
4.	Copy the Python script to fetch daily stock data from this repository, and add your API key
5.	Store the daily stock data (from the first run of the script) in your local storage to optimize API usage
6.	Copy the Python script to fetch the key metrics through the nested timeseries
7.	Your data pipeline is ready!
