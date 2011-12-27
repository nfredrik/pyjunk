import unittest
from morningstar import Morningstar
from dictionary import dict

class MorningstarTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)



    def testConstructor(self):
       
#       self.assertRaises(KeyError, Morningstar(' '))
        print Morningstar('didner')
        pass

    def testsenasteNAV(self):

       self.morningstar = Morningstar('didner')
       try:
           result = self.morningstar.senasteNAV()
           self.assertEqual(type(result), type(' '))
       finally:
           i = 0

if __name__ == '__main__':
    unittest.main()
