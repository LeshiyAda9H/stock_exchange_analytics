import requests
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class ListLevels:
    def print(self):
        securities = pd.read_csv('databases/securities_data.csv')
        print('Listing level 1:')
        for x in self.level1:
            print(list(securities.loc[securities['SECID'] == x]['SECNAME'])[0])
        print('\nListing level 2:')
        for x in self.level2:
            print(list(securities.loc[securities['SECID'] == x]['SECNAME'])[0])
        print('\nListing level 3:')
        for x in self.level3:
            print(list(securities.loc[securities['SECID'] == x]['SECNAME'])[0])

    def __init__(self):
        df = pd.read_csv('databases/securities_data.csv')
        self.level1 = df.loc[df['LISTLEVEL'] == 1]['SECID']
        self.level2 = df.loc[df['LISTLEVEL'] == 2]['SECID']
        self.level3 = df.loc[df['LISTLEVEL'] == 3]['SECID']
        self.levels = df['LISTLEVEL']

    def graph(self):
        plt.xlabel('Уровень листинга', fontsize=30)
        plt.ylabel('Кол-во компаний', fontsize=30)
        plt.hist(self.levels, 'auto', color='c', ec='0', lw=5)
        plt.show()
        pass