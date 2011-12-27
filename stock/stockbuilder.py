from dictionary import dict
from morningstar import Morningstar

class stockBuilder(object):
    def __init__(self):
        self.stocks = []
    def build_stocks(self):
        for d in dict:
            self.stocks.append(Morningstar(d))
        return self.stocks
