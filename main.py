from volume import *
from listlevels import *
from pe import *
from divd import *
import warnings

def main():
    warnings.filterwarnings("ignore")

    method1 = Volume()
    method1.very_popular_to_csv()
    method1.very_stable_to_csv()
    method1.popular_and_stable_to_csv()
    method1.graph()

    method2 = PE()
    method2.csv()

    method3 = ListLevels()
    method3.print()
    method3.graph()

    method4 = Divd()
    method4.csv()
    method4.graph()

    return 0

if __name__ == '__main__':
    main()