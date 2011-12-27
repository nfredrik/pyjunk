import unittest
from morningstar import Morningstar
from dictionary import dict
from mock import Mock, sentinel

teststr ='#title="Senaste NAV" style="width: 40%"><span class="value" style="width: 100%">  268,53 SEK</span></span><div style="clear: both;" class="section_separator"></div><h6 class="label" style="width: 50%" title="NAV http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P0000IWH7&programid=0000000000c-datum">NAV-datum<div class="helpbutton" style="display:inline;">'     

class MockTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def testsenasteNAV(self):

       morningstar = Morningstar('didner')

       #put the monkey patch in place
       morningstar.geturl = Mock()
       morningstar.geturl.return_value = teststr

       # fire away
       result = morningstar.senasteNAV()

#       print result

       self.assertTrue(morningstar.geturl.called)
       self.assertTrue(type(result), type(' '))

if __name__ == '__main__':
    unittest.main()
