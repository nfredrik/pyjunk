import unittest
from bin import Bin
from outcome import Outcome

class TestBin(unittest.TestCase):
    def setUp(self):
        self.first = Outcome('one', 17)
        self.second = Outcome('one', 17)
        self.third = Outcome('two', 32)

        self.fbin = Bin(self.first)
        self.sbin = Bin(self.second)

    def tearDown(self):
        pass

    def test___init__(self):
        self.assertTrue(isinstance(self.fbin, Bin))

    def test___str__(self):
        self.fbin.add(self.third)
        self.sbin.add(self.third)
        self.assertEqual(type(' '), type(self.fbin.__str__()))

    def test_add(self):
        # bin = Bin(*outcomes)
        # self.assertEqual(expected, bin.add(outcome))
        assert True # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
