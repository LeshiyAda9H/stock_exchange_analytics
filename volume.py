import requests
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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
        n = len(self.dispersions)
        self.dispersions.sort(key=lambda x: x[1])
        self.q1d = self.dispersions[int(n / 4)][1]
        self.q2d = self.dispersions[int(n / 2)][1]
        self.q3d = self.dispersions[int(n / 4 * 3)][1]
        self.medians.sort(key=lambda x: x[1])
        self.q1m = self.medians[int(n / 4)][1]
        self.q2m = self.medians[int(n / 2)][1]
        self.q3m = self.medians[int(n / 4 * 3)][1]

    def choose_very_stable(self):
        comp = set()
        for x in self.dispersions:
            if (self.q2m < x[1] < self.q3m + 1.5*(self.q3m-self.q1m) and
                self.q2d > x[1] > self.q1d - 1.5*(self.q3d-self.q1d)):
                comp.add(x[0])
        return comp

    def choose_popular_and_stable(self):
        comp = set()
        for x in self.medians:
            if self.q2m < x[1] < self.q3m + 1.5*(self.q3m-self.q1m):
                comp.add(x[0])
        return comp

    def choose_very_popular(self):
        comp = set()
        for x in self.medians:
            if x[1] >= self.q3m + 1.5*(self.q3m-self.q1m):
                comp.add(x[0])
        return comp

    def graph(self):
        m = [x[1] for x in list(self.medians) if x[1] < self.q3m + 1.5*(self.q3m-self.q1m)]
        plt.ylabel('Кол-во сделок', fontsize=30)
        plt.boxplot(m, label='Медиана = ' + str(self.q2m))
        plt.legend()
        plt.show()
        pass
