import requests
import pandas as pd
import numpy as np
import matplotlib as mpl

class ListLevels:
    def __init__(self):
        df = pd.read_csv('databases/securities_data.csv')
        self.level1 = 0
        self.level2 = 0
        self.level3 = 0
        for x in df['LISTLEVEL']:
            if x == 1:
                self.level1 += 1
            elif x == 2:
                self.level2 += 1
            else:
                self.level3 += 1

    def graph(self):
        pass