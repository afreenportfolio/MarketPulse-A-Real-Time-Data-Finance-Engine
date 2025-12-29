import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()

# Create the connection string
url_object = URL.create(
    "mysql+mysqlconnector",
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_NAME')
)

engine = create_engine(url_object)

# Pull the data into a DataFrame
df = pd.read_sql("SELECT * FROM ibm_daily_stock ORDER BY trade_date ASC", engine)

# Take a look at the first 5 rows
print(df.head())

# Calculate the 5-day moving average of the close price
df['ma_5'] = df['close_price'].rolling(window=5).mean()

# Check the results
print(df[['trade_date', 'close_price', 'ma_5']].head(10))

# Caluclate the daily percentage change
df['daily_return'] = df['close_price'].pct_change() * 100

#'Pulse' of the stock
print(df[['trade_date', 'close_price', 'daily_return']].tail(10))

# Creating the signal logic
df['signal'] = np.where(df['close_price'] > df['ma_5'], 'BUY', 'SELL')

# Transition points
print(df[['trade_date', 'close_price', 'ma_5', 'daily_return', 'signal']])

# Get a statistical summary of the prices and returns
summary = df[['close_price', 'daily_return']].describe()
print(summary)

# Get the date and the close_price on the day with max daily_return, and the date, close_price and daily_return of previous 2 days and the next two days, relative to the day with the max daily_return

# Find the index(row number) of the day with max daily_return
max_return_idx = df['daily_return'].idxmax()

# Define the range
context_window = df.iloc[max_return_idx - 2 : max_return_idx + 3]

# Select the columns
result = context_window[['trade_date', 'close_price', 'daily_return']]

print(result)

# Use the existing 'engine'
df.to_sql('ibm_analyzed_data', engine, if_exists='replace', index=False)
print("Analysis complete\nEnriched data saved to 'ibm_analyzed_data'.")
