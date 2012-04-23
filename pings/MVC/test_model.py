import unittest
from types import *

from model import Model

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        assert True

    def tearDown(self):
        del self.model
        assert True

    def test_get_date_4_object(self):
#        print self.model.get_date_4_object('oracle.com')
        self.assertEqual(list, type(self.model.get_date_4_object('oracle.com')))
#        self.assertIs( self.model.get_date_4_object('oracle.com'),ListType)


    def test_get_date_order(self):
        print self.model.get_date_order()
        self.assertEqual(list, type(self.model.get_date_order()))


    def test_get_pingobj_order(self):
        self.assertEqual(list, type(self.model.get_pingobj_order()))


    def test_get_response_order(self):
        self.assertEqual(list, type(self.model.get_response_order()))

    def test_get_ttl_order(self):
        self.assertEqual(list, type(self.model.get_ttl_order()))

    def test_write(self):
        self.assertEqual(NoneType, type(self.model.write(date= '2012-01-12', pingobj ='svards.eu', ttl= '23', response = '1')))

    def test_get_time_range(self):
        print self.model.get_time_range('svards.eu', '2012-01-12', '2012-04-01')
        
if __name__ == '__main__':
    unittest.main()
