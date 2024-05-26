import requests
import pandas as pd
import numpy as np
import matplotlib as mpl

class Divd:
    def csv(self):
        df = pd.DataFrame(self.divd_income, columns=['NAME','SECID','PRICE','DIVD','DIVDINCOME'])
        df.to_csv('databases/devincome.csv')

    def __init__(self):
        self.divd_income = []
        securities = pd.read_csv('databases/securities_data.csv')
        devs = pd.read_csv('databases/devs.csv')
        for x in devs['ID']:
            dev = float(devs.loc[devs['ID'] == x]['DEV'])
            try:
                price = float(securities.loc[securities['SECID'] == x]['PREVPRICE'])
                self.divd_income.append([list(securities.loc[securities['SECID'] == x]['SECNAME'])[0], x,
                                        price, dev, round(dev / price, 2)])
            except:
                pass