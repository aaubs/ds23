# https://www.alphavantage.co/

import os
from dotenv import load_dotenv
import pandas as pd
import json

import requests

#from functions import print_json_structure
load_dotenv()

api_key = os.getenv('FIN_API_KEY')


url = (
    f'https://www.alphavantage.co/query?'
    f'function=TIME_SERIES_DAILY&'
    f'symbol=AAPL&'
    f'apikey={api_key}'
)

response = requests.get(url)

data = response.json()


# Inspect Json structure
#print_json_structure(data)


# Convert the list of articles into a DataFrame
finance = data['Time Series (Daily)']
symbol = data['Meta Data']['2. Symbol']


df = pd.DataFrame(finance)

# Transpose the DataFrame
df_transposed = df.transpose()
df_transposed['Symbol'] = symbol

# Now, each column is an attribute (open, high, low, close, volume) and each row is a date.
print(df_transposed.head())