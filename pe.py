import requests
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class PE:
    def csv(self):
        df = pd.DataFrame(self.pes, columns = ['Name', 'ID', 'Capitalization', 'Income', 'P/E ratio'])
        df.to_csv('databases/PE.csv')

    def __init__(self):
        self.pes = []
        marketdata = pd.read_csv('databases/marketdata.csv')
        incomes = pd.read_csv('databases/income.csv')
        securities = pd.read_csv('databases/securities_data.csv')
        for x in marketdata['SECID']:
            cap = float(marketdata.loc[marketdata['SECID'] == x]['ISSUECAPITALIZATION'])
            if np.isnan(cap):
                continue
            try:
                income = float(incomes.loc[incomes['SECID'] == x]['INCOME'])
                pe = cap / income / 1000000000
                if pe > 0:
                    self.pes.append([list(securities.loc[securities['SECID'] == x]['SECNAME'])[0],
                    x, round(cap / 1000000000, 2), income, round(pe, 2)])
            except:
                pass

    def graph(self):
        m = [x[4] for x in list(self.pes) if x[4] < 35]
        m.sort()
        n = len(m)
        q1 = m[int(n/4)]
        q3 = m[int(n/4*3)]
        q2 = m[int(n/2)]
        plt.ylabel('P/E ratio', fontsize=30)
        plt.boxplot(m, label='Медиана = '+str(q2)+' Q1 = '+str(q1)+' Q3 = '+str(q3))
        plt.legend()
        plt.show()
