import requests
import pandas as pd
import matplotlib as mpl

start_date = '2023-01-01'
end_date = '2023-01-31'

def analyse(id):
    url = ('https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/' + id + '.json?from='
           + start_date + '&till=' + end_date + '&marketprice_board=1')
    response = requests.get(url)
    data = response.json()
    securities_data = data['history']
    df = pd.DataFrame(securities_data['data'], columns=securities_data['columns'])

def main():
    df = pd.read_csv('all_companies.csv')
    companies = df['SECID']
    for id in companies:
        analyse(id)
    return 0

if __name__ == '__main__':
    main()