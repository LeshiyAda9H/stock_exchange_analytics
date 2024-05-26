import requests
import pandas as pd
import numpy as np
import matplotlib as mpl

class PE:
    def bottom(self):
        df = pd.DataFrame(self.pes, columns = ['Name', 'ID', 'Capitalization', 'Income', 'P/E ratio'])
        df.to_csv('databases/PE.csv')

    def __init__(self):
        self.pes = []
        c1 = set()
        c2 = set()
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