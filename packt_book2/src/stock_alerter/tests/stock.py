from collections import namedtuple

_stock = namedtuple('mytuple','date','price')

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        #self.price = None
        self.price_history = []

    def update(self, date, price):
        if price < 0:
            raise ValueError("price should not be negative")
        #self.price_history.append((date,price))
        self.price_history.append(_stock(date=date,price=price))        

    @property
    def price(self):
        self.price_history.sort(key=lambda tup:tup.date)
        return self.price_history[-1].price if self.price_history else None
# not a good choice to return None, all should have same type.
        
    def is_increasing_trend(self):
        self.price_history.sort(key=lambda tup: tup.price)
        #print(self.price_history)
        return self.price_history[-3].price < self.price_history[-2].price < self.price_history[-1].price 
