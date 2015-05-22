import unittest
from datetime import datetime  # remark to writer sidan 18
from stock import Stock


class TestStock(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GLOOG")
        
    def test_stock_of_new_stock_object_should_be_None(self):     # remark to writer!  object instead of class
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """An update should set the price on the stock object
         We will be using the 'datetime' module for the timestamp
        """
        self.goog.update(datetime(2104, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        self.assertRaises(ValueError, self.goog.update, datetime(2014, 2, 13), -1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2104, 2, 12), price=10)
        self.goog.update(datetime(2104, 2, 13), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)

    def test_increasing_trend_is_true(self):
        timestamps = [datetime(2014, 2, 11), datetime(2014, 2, 12), datetime(2014, 2, 13)]
        prices = [8, 10, 12]
        
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

        self.assertTrue(self.goog.is_increasing_trend())

# These are not refactoring tests it's adding tests, remark
    def test_increasing_trend_is_false_if_price_decreases(self):
        timestamps = [datetime(2014, 2, 11), datetime(2014, 2, 12), datetime(2014, 2, 13)]
        prices = [8, 12, 10]
        
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal(self):
        timestamps = [datetime(2014, 2, 11), datetime(2014, 2, 12), datetime(2014, 2, 13)]
        prices = [8, 10, 10]
        
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

        self.assertFalse(self.goog.is_increasing_trend())


if __name__ == "__main__":
    unittest.main()
