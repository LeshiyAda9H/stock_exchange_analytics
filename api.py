import requests
import pandas as pd

# Получение данных через API MOEX
url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/securities.json'
response = requests.get(url)
data = response.json()

# Преобразование данных в pandas DataFrame
securities_data = data['history']
df = pd.DataFrame(securities_data['data'], columns=securities_data['columns'])
df.to_csv('all_companies.csv', index=False)