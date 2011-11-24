import unittest

from db  import PingDB

class TestPing(unittest.TestCase):
    def test__init__(self):
        self.assertTrue(True)

    def test_db(self):
        db = PingDB()       
        db.write('2011-11-10', 'sun.com', 334, 234)
        db.write('2011-11-12', 'oracle.com', 343, 324)
        print db.read_responses_order()

        print db.read_pingobj_order()

        print db.read_ttl_order()

        print db.read_date_order()

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

