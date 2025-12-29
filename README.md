## Phase 4: Stock Analysis

This phase involves transforming raw historical data into financial indicators to identify trends and generate trading signals.

### Features
- Developed a 5-day Moving Average (`ma_5`) to smooth out price volatility and identify the underlying trend.
- Calculated daily_return as a percentage to measure the daily "pulse" and intensity of price movements.
- Implemented a crossover strategy that generates a `BUY` signal when the `close_price` is above the `ma_5` and a `SELL` signal when it falls below.
- Created a secondary table, `ibm_analyzed_data`, to store these insights, ensuring the dashboard can access pre-calculated metrics for high performance.

### Database Schema
- The data is stored in a table named `ibm_analyzed_data` with the following structure:

`+--------------+--------+------+-----+---------+-------+`

`| Field        | Type   | Null | Key | Default | Extra |`

`+--------------+--------+------+-----+---------+-------+`

`| trade_date   | date   | YES  |     | NULL    |       |`

`| open_price   | double | YES  |     | NULL    |       |`

`| high_price   | double | YES  |     | NULL    |       |`

`| low_price    | double | YES  |     | NULL    |       |`

`| close_price  | double | YES  |     | NULL    |       |`

`| volume       | bigint | YES  |     | NULL    |       |`

`| ma_5         | double | YES  |     | NULL    |       |`

`| daily_return | double | YES  |     | NULL    |       |`

`| signal       | text   | YES  |     | NULL    |       |`

`+--------------+--------+------+-----+---------+-------+`

### Setup Instruction
1. Download `requirements.txt` and install the required libraries by running `pip install -r requirements.txt` in your terminal.
2. Copy/download the python script from this repository and run it using `python real_time_market_pulse_dashboard_stock_analyzer.py`

### Challenges
- When calculating the 5-day moving average, the first four rows of the dataset naturally lack enough preceding data to generate a result. To maintain a 5-day moving average, the first four days of any dataset lack sufficient history for a calculation. I had to ensure the logic accounted for these `NaN` (Not a Number) values to avoid calculation errors or broken visualizations in the future dashboard. To do this, I chose to preserve these as `NULL` values in the database to maintain data integrity. This ensures the archive remains an accurate historical record, while leaving the "cleanup" for the visualization layer in Phase 5.
- I discovered that a high positive return followed by a lower positive return is not a "crash," but rather a deceleration of growth. Learning to interpret the `daily_return` metric as the "intensity" of movement—rather than just the direction—was key to providing accurate analysis.
- Synchronizing two different tables (`ibm_daily_stock` and `ibm_analyzed_data`) required precise `INNER JOIN` logic. I had to ensure that the primary keys (`trade_dates`) matched perfectly and that typos in table references didn't break the query's ability to "summon" the combined dataset.
- Identifying the "peak" events required using advanced `Pandas` functions like `.idxmax()` and slicing techniques (`.iloc`) to retrieve not just a single data point, but the surrounding "context window" (days before and after) to understand the full story of a price spike.

### Final Output
- Final databse output can be gotten by running `SELECT * FROM ibm_analyzed_data;` in MySQL terminal
- Join your two tables together to compare raw prices with your new signals with `SELECT ibm_daily_stock.trade_date, ibm_daily_stock.close_price, ibm_analyzed_data.ma_5, ibm_analyzed_data.daily_return, ibm_analyzed_data.signal FROM ibm_daily_stock INNER JOIN ibm_analyzed_data ON ibm_daily_stock.trade_date = ibm_analyzed_data.trade_date ORDER BY ibm_daily_stock.trade_date ASC;` query in MySQL terminal.
