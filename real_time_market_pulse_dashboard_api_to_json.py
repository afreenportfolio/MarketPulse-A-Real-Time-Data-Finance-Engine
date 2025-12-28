import requests
import json
import mysql.connector
import os
from dotenv import load_dotenv

# 1. Your 'Digital ID'
API_KEY = os.getenv('Alpha_Vantage_Key') 

# 2. The 'Order' (URL)
# We are asking for 'TIME_SERIES_DAILY' which means prices minute-by-minute
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&interval=5min&apikey={API_KEY}'

# 3. Sending the request
response = requests.get(url)

# 4. Converting the 'meal' into a format Python understands (JSON)
data = response.json()

#Saving it to a local file
with open('data.json', 'w') as file:
    json.dump(data,file,indent=4)
    print("Data successfully saved to data.json")

# To read it back:
with open('data.json', 'r') as file:
    saved_data = json.load(file)
    print(saved_data)
