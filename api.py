import requests
import pandas as pd

url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/securities.json'
response = requests.get(url)
data = response.json()
history_data = data['history']
df = pd.DataFrame(history_data['data'], columns=history_data['columns'])
df.to_csv('history_data.csv', index=False)

url = 'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json'
response = requests.get(url)
data = response.json()
securities_data = data['securities']
df = pd.DataFrame(securities_data['data'], columns=securities_data['columns'])
df.to_csv('securities_data.csv', index=False)
marketdata = data['marketdata']
df = pd.DataFrame(marketdata['data'], columns=marketdata['columns'])
df.to_csv('marketdata.csv', index=False)