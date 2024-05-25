import requests
import pandas as pd
import matplotlib.pyplot as plt

# # Получение данных через API MOEX
# url = 'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json'
# response = requests.get(url)
# data = response.json()
#
# # Преобразование данных в pandas DataFrame
# securities_data = data['securities']
# df = pd.DataFrame(securities_data['data'], columns=securities_data['columns'])
# df.to_csv('df.csv', index=False)

# Получение данных через API MOEX
url = 'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/columns.json'
response = requests.get(url)
data = response.json()

# Преобразование данных в pandas DataFrame
securities_data = data['securities']
df = pd.DataFrame(securities_data['data'], columns=securities_data['columns'])
df.to_csv('columns.csv', index=False)