import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


from functions import print_json_structure

# air quality
url = (
    f'https://air-quality-api.open-meteo.com/v1/'
    f'air-quality?'
    f'latitude={45.804}&longitude={15.1689}'
    f'&hourly=european_aqi'
    f'&past_days=2'
)

print(url)

response = requests.get(url)
print(response)

data = response.json()
print_json_structure(data)


df_airquality = pd.DataFrame(data['hourly'])

df_airquality['latitude']= data['latitude']
df_airquality['longitude']= data['longitude']


# temperature

url = (
    f'https://api.open-meteo.com/v1/'
    f'forecast?'
    f'latitude={45.804}&longitude={15.1689}'
    f'&hourly=temperature_2m,wind_speed_10m'
    f'&past_days=2'
)
response = requests.get(url)
print(response)

data = response.json()

df_weather = pd.DataFrame(data['hourly'])

# Merge two dataframes with key 'time'
df =pd.merge(left=df_airquality, right=df_weather, on='time')


# Filtering to get one 'time' per day at 00:00
df['time'] = pd.to_datetime(df['time'])

ticks = df[df['time'].dt.hour == 0]['time']

# Plot setup
plt.figure(figsize=(10, 6))

# Plotting the data
plt.plot(df['time'], df['european_aqi'], label='European AQI', marker='o')
plt.plot(df['time'], df['temperature_2m'], label='Temperature 2m (°C)', marker='s')
plt.plot(df['time'], df['wind_speed_10m'], label='Wind Speed 10m (m/s)', marker='^')

# Setting x-axis ticks to only those at 00:00
plt.gca().set_xticks(ticks)

# Formatting x-axis labels to display date and ensure "00:00" is implicit
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Environmental Conditions Over Time in Novo mesto')
plt.legend()

# Rotate date labels for better readability
plt.xticks(rotation=45)

plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()