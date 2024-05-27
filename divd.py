from header import *

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

    def graph(self):
        plt.xlabel('Цена акции', fontsize=30)
        plt.ylabel('Див. доходность', fontsize=30)
        self.divd_income.sort(key=lambda x : x[2])
        x = [x[2] for x in self.divd_income]
        y = [x[4] for x in self.divd_income]
        plt.scatter(x,y, color='0')
        plt.plot(x, y, color='g')
        plt.show()
        plt.xlabel('Цена акции', fontsize=30)
        plt.ylabel('Див. доходность', fontsize=30)
        x = [x[2] for x in self.divd_income if x[2] < 1000]
        y = [x[4] for x in self.divd_income if x[2] < 1000]
        plt.scatter(x, y, color='0')
        plt.plot(x, y, color='g')
        plt.show()
        plt.xlabel('Цена акции', fontsize=30)
        plt.ylabel('Див. доходность', fontsize=30)
        x = [x[2] for x in self.divd_income if x[2] < 250]
        y = [x[4] for x in self.divd_income if x[2] < 250]
        plt.scatter(x, y, color='0')
        plt.plot(x, y, color='g')
        plt.show()
