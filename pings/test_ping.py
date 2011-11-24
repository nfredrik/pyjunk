import unittest

from ping  import Ping

class TestPing(unittest.TestCase):
    def test__init__(self):
        self.assertTrue(True)

    def test_first(self):
        pinga = Ping('sun.com')       

        print pinga.get_ttl()
        print pinga.get_response()
        print pinga.get_time()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

