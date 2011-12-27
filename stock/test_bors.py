import unittest
import re

from bors import Bors

class BorsTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.bors = Bors()

    def checkMatch(self, match):
          if match is None:
               return False

          return True


    def testIndex(self):
        try:
            result = self.bors.getindex()
        finally:
            self.valid = re.compile(r'\d\{3}\.\d{2}')
            # a better check of the result
            self.valid = re.compile(r'\d{3}\.\d{2}')  # eg 357.57
            self.assertTrue(self.checkMatch(self.valid.match(result)))
  
    def testDeviation(self):
        result = self.bors.getdeviation()
        self.valid = re.compile(r'[-+]\d{1,2}\.\d{1,2}')  # eg +/-0.79
        self.assertTrue(self.checkMatch(self.valid.match(result)))



if __name__ == '__main__':
    unittest.main()


