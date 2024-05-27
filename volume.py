from header import *
import requests

start_date = '2023-05-01'
end_date = '2024-06-01'

class Volume:
    def analyse(self, c):
        data = requests.get(('https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/' + c +
                             '.json?from=' + start_date + '&till=' + end_date + '&marketprice_board=1')).json()
        df = pd.DataFrame(data['history']['data'], columns=data['history']['columns'])
        for x in df['LOW']:
            if pd.isnull(x):
                return
        for x in df['HIGH']:
            if pd.isnull(x):
                return
        for x in df['VALUE']:
            if pd.isnull(x):
                return
        middle_price = df['LOW'] + df['HIGH']
        amounts = 2 * df['VALUE'] / middle_price
        median = amounts.median()
        self.medians.append((c, int(median)))
        dispersion = []
        for x in amounts:
            dispersion.append((x - median)**2)
        self.dispersions.append((c, int(np.median(dispersion))))

    def __init__(self):
        self.dispersions = []
        self.medians = []
        df = pd.read_csv('databases/history_data.csv')
        companies = df['SECID']
        for c in companies:
            self.analyse(c)
        n = len(self.dispersions)
        self.dispersions.sort(key=lambda x: x[1])
        self.q1d = self.dispersions[int(n / 4)][1]
        self.q2d = self.dispersions[int(n / 2)][1]
        self.q3d = self.dispersions[int(n / 4 * 3)][1]
        self.medians.sort(key=lambda x: x[1])
        self.q1m = self.medians[int(n / 4)][1]
        self.q2m = self.medians[int(n / 2)][1]
        self.q3m = self.medians[int(n / 4 * 3)][1]

    def choose_very_stable(self):
        comp = set()
        for x in self.medians:
            if (self.q2m < x[1] < self.q3m + 1.5*(self.q3m-self.q1m) and
                self.q2d > x[1] > self.q1d - 1.5*(self.q3d-self.q1d)):
                comp.add(x[0])
        return comp

    def choose_popular_and_stable(self):
        comp = set()
        for x in self.medians:
            if self.q2m < x[1] < self.q3m + 1.5*(self.q3m-self.q1m):
                comp.add(x[0])
        return comp

    def choose_very_popular(self):
        comp = set()
        for x in self.medians:
            if x[1] >= self.q3m + 1.5*(self.q3m-self.q1m):
                comp.add(x[0])
        return comp

    def very_stable_to_csv(self):
        data = []
        medians = dict(self.medians)
        dispersions = dict(self.dispersions)
        history = pd.read_csv('databases/history_data.csv')
        for x in self.choose_very_stable():
            data.append([list(history.loc[history['SECID'] == x]['SHORTNAME'])[0], x, medians[x], dispersions[x]])
        pd.DataFrame(data, columns = ['SHORTNAME', 'SECID', 'MEDIAN', 'DISPERTION']).to_csv('databases/very_stable.csv')

    def popular_and_stable_to_csv(self):
        data = []
        medians = dict(self.medians)
        history = pd.read_csv('databases/history_data.csv')
        for x in self.choose_popular_and_stable():
            data.append([list(history.loc[history['SECID'] == x]['SHORTNAME'])[0], x, medians[x]])
        pd.DataFrame(data, columns = ['SHORTNAME', 'SECID', 'MEDIAN']).to_csv('databases/popular_and_stable.csv')


    def very_popular_to_csv(self):
        data = []
        medians = dict(self.medians)
        history = pd.read_csv('databases/history_data.csv')
        for x in self.choose_very_popular():
            data.append([list(history.loc[history['SECID'] == x]['SHORTNAME'])[0], x, medians[x]])
        pd.DataFrame(data, columns = ['SHORTNAME', 'SECID', 'MEDIAN']).to_csv('databases/very_popular.csv')

    def graph(self):
        m = [x[1] for x in list(self.medians) if x[1] < self.q3m + 1.5*(self.q3m-self.q1m)]
        plt.ylabel('Кол-во сделок', fontsize=30)
        plt.boxplot(m, label='Медиана = ' + str(self.q2m))
        plt.legend()
        plt.show()
        pass
