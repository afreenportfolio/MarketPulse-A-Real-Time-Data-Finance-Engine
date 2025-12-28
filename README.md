# MarketPulse-A-Real-Time-Data-Finance-Engine
MarketPulse: An end-to-end data engineering project featuring a robust Python pipeline, local JSON caching for API optimization, and a SQL-backed historical data warehouse.

## Phase 1: Data Pipeline
1. I developed a Python script to fetch daily stock data (IBM) via Alpha Vantage API.
2. I stored the daily stock data in a JSON file (with proper formatting to prevent formatting errors) to optimize API usage.
3. Developed a Python script that iterates through nested timeseries data to extract key metrics (Open, High, Low, Close, Volume)

### Challenge:
- Initial raw data from Python IDLE used single quotes (''), which caused json.decode errors as the standard JSON format requires double quotes ("").
- This was fixed by implementing a manual data sanitation step (and exploring automated string replacement) to ensure the local storage strictly follows JSON standards and seamlessly parses with Python's json library

### Setup Instructions:
1. Install the required libraries by running pip install -r requirements.txt in your terminal.
2. Navigate to the Alpha Vantage Support Page
3. Sign up (it's free!)
4. Save the API key you get securely in a .env file with the format VARIABLE_NAME=YOUR_KEY.
5. Copy the Python script to fetch daily stock data from this repository.
6. Uncomment the section that uses the API key to get the daily stock data
7. Store the daily stock data (from the initial run of the script) in your local storage to optimize API usage
8. Comment out the section that uses the API key, and uncomment the section that uses your local file with the daily stock data.
9. Rename the file name "local_file.json" (in the line "with open('local_file.json', 'r') as file:") with the name of the file which stores the daily stock data from the initial script run.
10. Run the Python script to fetch the key metrics through the nested timeseries
11. Your data pipeline is ready!
