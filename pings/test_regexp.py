import unittest
import re

from regexp  import RegExp



class TestPing(unittest.TestCase):



    def test_first(self):

        pattern = "^[a-z]+(\.[a-z]+)+$"
#        print 'FIRST:',  re.match("^[a-z]+(\.[a-z]+)+$", "www.sun.com")
        
#        if m : print 'we got a match'


        i = RegExp(pattern, "www.sun.com")
        self.assertTrue(i())

        n = RegExp(pattern, "ftp.sunet.se")
        self.assertTrue(n())

        pelle = RegExp(pattern, "ftp.sunet.se")
        self.assertTrue(pelle())

    def test_second(self):

        # Look ahead insertion ...
        p = RegExp('Isaac (?=Asimov)','Isaac Asimov')
        self.assertTrue(p())

        # Negative look ahead
        k = RegExp('Isaac (?!Asimov)','Isaac Bsimov')
        self.assertTrue(k())

if __name__ == '__main__':
    unittest.main()

