from volume import *
from listlevels import *
from pe import *
from divd import *
import json
import pandas as pd
import warnings

def main():
    warnings.filterwarnings("ignore")
    # method1 = Volume()
    # print(method1.choose_very_popular())
    # print(method1.choose_popular_and_stable())
    # print(method1.choose_very_stable())
    #method2 = ListLevels()
    #method2.print()
    method4 = Divd()
    method4.csv()
    return 0

if __name__ == '__main__':
    main()