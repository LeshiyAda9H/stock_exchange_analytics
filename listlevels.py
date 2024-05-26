import requests
import pandas as pd
import numpy as np
import matplotlib as mpl

class ListLevels:
    def __init__(self):
        df = pd.read_csv('databases/securities_data.csv')
        self.level1 = df.loc[df['LISTLEVEL'] == 1]['SECID']
        self.level2 = df.loc[df['LISTLEVEL'] == 2]['SECID']
        self.level3 = df.loc[df['LISTLEVEL'] == 3]['SECID']
        self.levels = df['LISTLEVEL']

    def graph(self):
        pass