import requests
import pandas as pd
import numpy as np
import matplotlib as mpl

start_date = '2024-01-01'
end_date = '2024-05-01'

class Volume:
    def analyse(self, c):
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
        self.medians.append((c, int(median)))
        dispersion = []
        for x in amounts:
            dispersion.append((x - median)**2)
        self.dispersions.append((c, int(np.median(dispersion))))

    def __init__(self):
        self.dispersions = []
        self.medians = []
        df = pd.read_csv('databases/history_data.csv')
        companies = df['SECID']
        for c in companies:
            self.analyse(c)

    def choose_good_securities(self):
        n = len(self.dispersions)
        self.dispersions.sort(key=lambda x: x[1])
        q1d = self.dispersions[int(n / 4)][1]
        q2d = self.dispersions[int(n / 2)][1]
        q3d = self.dispersions[int(n / 4 * 3)][1]
        self.medians.sort(key=lambda x: x[1])
        q1m = self.medians[int(n / 4)][1]
        q2m = self.medians[int(n / 2)][1]
        q3m = self.medians[int(n / 4 * 3)][1]
        good = set()
        self.medians = dict(self.medians)
        for x in self.dispersions:
            dispersion = x[1]
            median = self.medians[x[0]]
            if q2m >= median >= q1m - 1.5*(q3m - q1m):
                good.add(x[0])

    def graph(self):
        pass