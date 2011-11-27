import unittest

from db  import PingDB


class TestPing(unittest.TestCase):
    def test__init__(self):
        self.assertTrue(True)

    def test_db(self):
        db = PingDB()       
        db.write('2011-11-10', 'sun.com', 334, 234)
        db.write('2011-11-12', 'oracle.com', 343, 324)
        db.read_responses_order()

        db.read_pingobj_order()

        db.read_ttl_order()

        db.read_date_order()

        db.read_date_4_object('sun.com')

        self.list = db.read_date_4_object('oracle.com')

        for i in self.list:
            print i


        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

