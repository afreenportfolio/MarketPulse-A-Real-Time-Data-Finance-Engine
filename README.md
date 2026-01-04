## Phase 3: MySQL Data Pipeline

This phase focuses on taking the raw stock data stored in `data.json` and adding it into a structured MySQL relational database.

### Features

- Reads local JSON data and prepares it for SQL insertion.
- Uses `INSERT ... ON DUPLICATE KEY UPDATE` to ensure data stays fresh without creating duplicate date entries.
- Designed to build a long-term historical record. By appending new daily data while preserving previous entries, the database grows beyond the 100-day limit of the standard "Compact" API response, enabling long-term trend analysis.
- Utilizes `.env` files to keep database credentials secure.

### Database Schema

- The data is stored in a table named `ibm_daily_stock` with the following structure:

`+-------------+---------------+------+-----+---------+-------+`

`| Field       | Type          | Null | Key | Default | Extra |`

`+-------------+---------------+------+-----+---------+-------+`

`| trade_date  | date          | NO   | PRI | NULL    |       |`

`| open_price  | decimal(10,4) | YES  |     | NULL    |       |`

`| high_price  | decimal(10,4) | YES  |     | NULL    |       |`

`| low_price   | decimal(10,4) | YES  |     | NULL    |       |`

`| close_price | decimal(10,4) | YES  |     | NULL    |       |`

`| volume      | bigint        | YES  |     | NULL    |       |`

`+-------------+---------------+------+-----+---------+-------+`

### Setup & Installation

1. Download `requirements.txt` and install the required libraries by running `pip install -r requirements.txt` in your terminal.
2. Create the database and table in MySQL terminal.
   - `CREATE DATABASE real_time_market_pulse_dashboard;`
   - `USE real_time_market_pulse_dashboard;`
   - `CREATE TABLE ibm_daily_stock(trade_date DATE PRIMARY KEY, open_price DECIMAL(10,4),high_price DECIMAL(10,4),low_price DECIMAL(10,4),close_price DECIMAL (10,4),volume BIGINT);`
4. Add your `DB_HOST=localhost`, `DB_USER=root`, `DB_PASSWORD='YOUR_ACTUAL_MYSQL_PASSWORD'`, and `DB_NAME=real_time_market_pulse_dashboard` to your .env file.
5. Copy/download the python script from this repository and run it using `python real_time_market_pulse_dashboard_mysql_integration.py`

### Challenges

- Selecting the correct data types to ensure financial data accuracy. Used `DECIMAL(10,4)` for stock prices instead of `FLOAT` or `DOUBLE` to avoid `floating-point errors` that can occur during financial calculations, and used `BIGINT` for volume to accommodate high-frequency trading numbers.
- Preventing the script from crashing or creating duplicate rows if the same data was uploaded more than once (e.g., if the script was ran twice on the same day). Implemented the `INSERT ... ON DUPLICATE KEY UPDATE` logic. This ensures the database stays clean and reflects the most recent data without errors.
- Encountering the ProgrammingError: `Cursor is not connected` error. Leart about Python indentation and loop logic. The connection and cursor were being closed inside the loop after the first record, rather than outside the loop after all 100 records were processed.
- Receiving the `io.UnsupportedOperation: not readable` error. Understood file "modes" in Python. I realized that a file opened for writing ('w') cannot be read from simultaneously. The solution was to properly close the write-stream before opening a new read-stream ('r').
- Keeping sensitive database passwords and API keys out of the source code to follow security best practices. Integrated the `python-dotenv` library to pull credentials from a local `.env` file, ensuring they aren't accidentally pushed to a public GitHub repository.

### Final Database Output

- Final databse output can be gotten by running `SELECT * FROM ibm_daily_stock;` in MySQL terminal
