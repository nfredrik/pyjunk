from morningstar import Morningstar
from stockbuilder import stockBuilder
import sys

def main():
    args = sys.argv[1:]

    stockbuilder = stockBuilder("stocks.json")

    stocks = stockbuilder.build_stocks()

    for s in stocks:
        print (s.__str__, s.senasteNAV())

if __name__ == '__main__':
  main()
