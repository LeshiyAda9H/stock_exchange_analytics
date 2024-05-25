import pandas as pd
import matplotlib as mpl

def main():
    df = pd.read_csv('one_company_data.csv')
    print(abs(df['LEGALCLOSEPRICE'] - df['OPEN']))
    return 0

if __name__ == '__main__':
    main()