import requests
import pandas as pd
import numpy as np
import matplotlib as mpl

class PE:
    def __init__(self):
        self.pes = []
        c1 = set()
        c2 = set()
        marketdata = pd.read_csv('databases/marketdata.csv')
        incomes = pd.read_csv('databases/income.csv')
        for x in marketdata['SECID']:
            cap = float(marketdata.loc[marketdata['SECID'] == x]['ISSUECAPITALIZATION'])
            if np.isnan(cap):
                continue
            try:
                income = float(incomes.loc[incomes['SECID'] == x]['INCOME'])
                self.pes.append(cap / income / 1000000000)
            except:
                pass
        for x in self.pes:
            print(x)