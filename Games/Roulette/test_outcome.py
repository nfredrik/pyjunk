import unittest
from outcome import Outcome

class TestOutcome(unittest.TestCase):
    def setUp(self):
        self.first = Outcome('one', 17)
        self.second = Outcome('one', 17)
        self.third = Outcome('two', 32)

    def test___eq__(self):
        # outcome = Outcome(name, odds)
        # self.assertEqual(expected, outcome.__eq__(other))
        self.assertTrue(self.first == self.second)

    def test___ne__(self):
        # outcome = Outcome(name, odds)
        # self.assertEqual(expected, outcome.__ne__(other))
        self.assertTrue(self.first != self.third)

    def test___id_comparision(self):
        # outcome = Outcome(name, odds)
        # self.assertEqual(expected, outcome.__str__())
        print id(self.first)
        print id(self.second)
        self.assertTrue(self.first is self.second)

    def test_winAmount(self):
        # outcome = Outcome(name, odds)
        # self.assertEqual(expected, outcome.winAmount(amount))
        self.assertTrue((2 * 32) == self.third.winAmount(2))

    def tearDown(self):
        first = second = third = None
        pass

if __name__ == '__main__':
    unittest.main()
