from enum import Enum
from timeseries import *
import bisect
from collections import namedtuple

_stock = namedtuple('mytuple','date price')

class StockSignal(Enum):
    buy = 1
    neutral = 0
    sell = -1


class Stock:
    LONG_TERM_TIMESPAN = 10
    SHORT_TERM_TIMESPAN = 5
    def __init__(self, symbol):
        self.symbol = symbol
        #self.price = None
        self.price_history = []

    def _old_update(self, date, price):
        if price < 0:
            raise ValueError("price should not be negative")
        #self.price_history.append((date,price))
        self.price_history.append(_stock(date=date,price=price))        

    def update(self, date, price):
        if price < 0:
            raise ValueError("price should not be negative")

        bisect.insort_left(self.price_history, Update(timestamp, price))    
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

    def _get_closing_price_list(self, on_date, num_days):
        closing_price_list = []
        for i in range(num_days):
            chl = on_date.date() - timedelta(i)
            for price_event in reversed(self.price_history):
                if price_event.timestamp.date() > chk:
                    pass
                if price_event.timestamp.date ==  chk:
                    closing_price_list.insert(0, price_event)
                    break
                if price_event.timestamp.date() > chk:
                    closing_price_list.insert(0, price_event)                    
                    break      

        return closing_price_list

    def get_crossover_signal(self, on_date):
        closing_price_list = []
        NUM_DAYS = self.LONG_TERM_TIMESPAN +1
        closing_price_list = self._get_closing_price_list(on_date, NUM_DAYS)
        
        # Return NEUTRAL get_crossover_signal
        if len(closing_price_list) < 11:
            pass