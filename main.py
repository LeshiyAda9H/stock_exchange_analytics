import requests
import pandas as pd
import numpy as np
import matplotlib as mpl

start_date = '2024-01-01'
end_date = '2024-05-01'
dispersions = []
medians = []

def analyse(c):
    # загружаем БД и создаём датафрейм
    url = ('https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/' + c + '.json?from='
           + start_date + '&till=' + end_date + '&marketprice_board=1')
    response = requests.get(url)
    data = response.json()
    securities_data = data['history']
    df = pd.DataFrame(securities_data['data'], columns=securities_data['columns'])
    for x in df['LOW']:
        if pd.isnull(x):
            return
    for x in df['HIGH']:
        if pd.isnull(x):
            return
    middle_price = df['LOW'] + df['HIGH']
    amounts = 2 * df['VALUE'] / middle_price
    median = amounts.median()
    global dispersions
    global medians
    medians.append((c, int(median)))
    dispersion = []
    for x in amounts:
        dispersion.append((x - median)**2)
    dispersions.append((c, int(np.median(dispersion))))

def main():
    df = pd.read_csv('history_data.csv')
    companies = df['SECID']
    #analyse('GAZP')
    for c in companies:
        analyse(c)
    global dispersions
    n = len(dispersions)
    dispersions.sort(key=lambda x: x[1])
    q1d = dispersions[int(n / 4)][1]
    q2d = dispersions[int(n / 2)][1]
    q3d = dispersions[int(n / 4 * 3)][1]
    global medians
    medians.sort(key=lambda x: x[1])
    q1m = medians[int(n / 4)][1]
    q2m = medians[int(n / 2)][1]
    q3m = medians[int(n / 4 * 3)][1]
    box1 = set()
    box2 = set()
    medians = dict(medians)
    # for x in dispersions:
    #     dispersion = x[1]
    #     median = medians[x[0]]
    #     if q2m >= median >= q1m - 1.5*(q3m - q1m):
    #         box1.add(x[0])

    for x in dispersions:
        dispersion = x[1]
        median = medians[x[0]]
        if q1d - 1.5*(q3d - q1d) <= dispersion <= q2d:
            box1.add(x[0])
        if q2m <= median <= q1m + 1.5*(q3m - q1m):
            box2.add(x[0])

    #Выбросы = наблюдения > Q3 + 1,5*IQR или Q1 – 1,5*IQR
    print(box1)
    print(box2)
    return 0

if __name__ == '__main__':
    main()