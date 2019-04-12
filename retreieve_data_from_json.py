import requests
import matplotlib.pyplot as plt
import numpy as np

query_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=GOOGL&apikey=RC90TGA5BKPHHRVT"

response = requests.get(query_url)
global data
data = response.json()

close = []
dates = []

for i in data["Time Series (Daily)"]:
    close.append(data["Time Series (Daily)"][i]["4. close"])
    dates.append(i)


print(close)