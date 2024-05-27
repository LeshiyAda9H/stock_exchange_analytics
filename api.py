import requests
import pandas as pd

data = requests.get('https://iss.moex.com/iss/history/engines/stock/markets/shares/securities.json').json()
pd.DataFrame(data['history']['data'], columns=data['history']['columns']).to_csv('databases/history_data.csv', index=False)

# data = requests.get('https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/columns.json').json()
# pd.DataFrame(data['history']['data'], columns=data['history']['columns']).to_csv('columns_descriptions/history_data.csv', index=False)

data = requests.get('https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json').json()
pd.DataFrame(data['securities']['data'], columns=data['securities']['columns']).to_csv('databases/securities_data.csv', index=False)
pd.DataFrame(data['marketdata']['data'], columns=data['marketdata']['columns']).to_csv('databases/marketdata.csv', index=False)

# data = requests.get('https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/columns.json').json()
# pd.DataFrame(data['securities']['data'], columns=data['securities']['columns']).to_csv('columns_descriptions/securities_data.csv', index=False)
# pd.DataFrame(data['marketdata']['data'], columns=data['marketdata']['columns']).to_csv('columns_descriptions/marketdata.csv', index=False)