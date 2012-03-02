import unittest
from netstat import Netstat

class TestNetstat(unittest.TestCase):
    def test___init__(self):
        # netstat = Netstat()
        assert True # TODO: implement your test here

    def test_get_port_status(self):
        netstat = Netstat()
        self.assertEqual('LISTEN', netstat.get_port_status(631))

if __name__ == '__main__':
    unittest.main()
