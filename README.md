## Phase 1: API to JSON

This phase focuses on getting the IBM daily stock exchange data using an API key and storing that static data into a JSON file for further processing

## Features

- Accessing the API key securely using `os.getenv()`.
- Getting the prices day-by-day
- Converting the raw data into JSON format
- Saving the JSON data into a local file and verifying it by reading it back

### Setup Instructions

1. Install the required libraries by running `pip install -r requirements.txt` in your terminal.
2. Navigate to the Alpha Vantage Support Page
3. Sign up (it's free!)
4. Save the API key you get securely in a `.env` file with the format `VARIABLE_NAME=YOUR_KEY`.
5. Copy/download the Python script and run it using `python real_time_market_pulse_dashboard_api_to_json.py` to fetch daily stock data from this repository.
6. Run the Python script to fecth data using API and save it to a JSON file (named `data.json`) to optimize API usage.
7. Your final data for creating the dashboard is ready!

### Challenge:

- Initial raw data was saved to the JSON file as one cramped line.
- Used `indent=4` argument while "dumping" the JSON file to make the data human readable.
- Used `w` (write-only) argument to create the JSON file and to write to the JSON file.
- Used the `r` (read-only) argument to read and verify the data back from the file to the Python IDLE.
