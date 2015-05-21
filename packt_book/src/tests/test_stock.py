import unittest
from ..stock import Stock

class StockTest(unittest.TestCase):
	def test_price_of_new_stock_class_should_None(self):
		stock = Stock("GOOG")
		self.assertIsNone(stock.price)
