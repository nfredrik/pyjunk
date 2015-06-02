import unittest
from datetime import datetime  # remark to writer sidan 18
from datetime import timedelta
from ..stock import Stock
import collections
import sys


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
        self.goog.update(datetime(2104, 2, 13), price=10)
        self.goog.update(datetime(2104, 2, 12), price=8.4)
        self.assertAlmostEqual(10, self.goog.price, delta=0.0001)

    def test_price_is_the_latest_even_if_updates_are_made_out_of_order(self):
        self.goog.update(datetime(2014, 2, 13), price=8)
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(8, self.goog.price)



class StockTrendTest(unittest.TestCase):
    def given_a_series_of_prices(self, goog, prices):
        timestamps = [datetime(2014, 2, 11), datetime(2014, 2, 12), datetime(2014, 2, 13)]
        for timestamp, price in zip(timestamps, prices):
            goog.update(timestamp, price)        

    def test_stock_trends(self):
        dataset = [
        ([8,10,12], True),
        ([8,12,10], False),
        ([8,10,10], False)
        ]
        for data in dataset:
            prices, output = data
            with self.subTest(prices=prices, output=output):
                goog = Stock("GOOG")
                self.given_a_series_of_prices(goog,prices)
                self.assertEqual(output, goog.is_increasing_trend())

    # def test_increasing_trend_is_true(self):
    #     prices = [8, 10, 12]
    #     self.given_a_series_of_prices(goog, prices)    
    #     self.assertTrue(self.goog.is_increasing_trend())

    # def test_increasing_trend_is_false_if_price_decreases(self):
    #     prices = [8, 12, 10]    
    #     self.given_a_series_of_prices(prices)    
    #     self.assertFalse(self.goog.is_increasing_trend())

    # def test_increasing_trend_is_false_if_price_equal(self):
    #     prices = [8, 10, 10]
    #     self.given_a_series_of_prices(prices)            
    #     self.assertFalse(self.goog.is_increasing_trend())
        

class StockCrossOverSignalTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    def _flatten(self, timestamps):
        """Yield timestamp, if not recursivly call until we are"""
        for timestamp in timestamps:
            if not isinstance(timestamp, collections.Iterable):
                yield timestamp
            else:
                for value in self._flatten(timestamp):
                    yield value

    def _genererate_timestamps_date(self, date, price_list):
        """Generate a list of datetime objects with different dates"""
        if not isinstance(price_list, collections.Iterable):
            return date
        else:
            sys.exit(2)
            delta = 1.0/len(price_list)
            print("delta:{}".format(delta))
            return [date + i*timedelta(delta) for i in range(len(price_list))]

    def _old_generate_timestamps(self, price_list):

        return list(self._flatten([
            self._genererate_timestamps_date(datetime(2014, 2, 13) -
                                            timedelta(i),
                                            price_list[len(price_list)-i-1])

            for i in range(len(price_list) -1, -1, -1)
            if price_list[len(price_list) -i -1] is not None]))

    def _generate_timestamps(self, price_list):

        return [datetime(2014, 2, 13) - timedelta(i)
                    for i in range(len(price_list) -1, -1, -1)
                    if price_list[len(price_list) -i -1] is not None]

    def given_a_series_of_prices(self, price_list):
        timestamps = self._generate_timestamps(price_list)
        for timestamp, price in zip(timestamps,
                                    list(self._flatten([p
                                                        for p in price_list
                                                        if p is not None]))):
            self.goog.update(timestamp, price)


    def test_generate_timestamp_return_consecutive_dates(self):
        price_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected = [
                    datetime(2014,2,3), datetime(2014,2,4), datetime(2014,2,5), 
                    datetime(2014,2,6), datetime(2014,2,7), datetime(2014,2,8), 
                    datetime(2014,2,9), datetime(2014,2,10), datetime(2014,2,11),
                    datetime(2014,2,12), datetime(2014,2,13)                      
                    ]

        self.assertEqual(expected, self._generate_timestamps(price_list))


    def test_generate_timestamp_skips_empty_dates(self):
        pass

    def test_generate_timestamp_handles_multiple_updates_per_date(self):
        pass

    def test_stock_with_less_data_returns_neutral(self):
        pass

    def test_with_downward_crossover_returns_sell(self):
        pass

    def test_with_upward_crossover_returns_buy(self):
        pass

    def test_should_only_look_at_closing_rate(self):
        pass

    def test_should_be_neutral_if_not_enoguh_days_of_data(self):
        pass

    def test_should_pick_up_previous_closing_if_no_updates_for_a_day(self):
        pass

    def test_should_have_11_days_worth_of_data(self):
        pass

    def test_date_to_check_can_be_beyond_last_update_date(self):
        pass


if __name__ == "__main__":
    unittest.main()
