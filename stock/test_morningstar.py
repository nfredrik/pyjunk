import unittest
from morningstar import Morningstar
from dictionary import dict

class MorningstarTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)



    def testConstructor(self):
       self.morningstar = Morningstar(' ')
       self.assertRaises(IOError, self.morningstar.senasteNAV)

    def testsenasteNAV(self):

       self.morningstar = Morningstar(dict['didner'])
       try:
           result = self.morningstar.senasteNAV()
           self.assertEqual(type(result), type(' '))
       finally:
           i = 0

if __name__ == '__main__':
    unittest.main()
