# https://newsapi.org/

import os
from dotenv import load_dotenv
import pandas as pd
import json

import requests

#from functions import print_json_structure
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv('NEWS_API_KEY')


url = (
    f'https://newsapi.org/v2/everything?'
    f'q=GPT&'
    f'from=2024-02-29&'
    f'to=2024-03-11&'
    f'apiKey={api_key}'
)

response = requests.get(url)

data = response.json()


####### Json to data frame

# Inspect the structure of the json file
#print_json_structure(data)



# Convert the list of articles into a DataFrame
articles = data['articles']
df = pd.DataFrame(articles)

# Expand the 'source' column into separate columns
df_source = df['source'].apply(pd.Series)
df_source.columns = [f"source_{colname}" for colname in df_source.columns]

# Concatenate the expanded source DataFrame with the original DataFrame
df = pd.concat([df.drop(['source'], axis=1), df_source], axis=1)

print(df.head())



