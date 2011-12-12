import unittest
import re

from ping  import Ping

class TestPing(unittest.TestCase):
    def test__init__(self):
        self.assertTrue(True)

    def test_first(self):
        pinga = Ping('sun.com')       

        self.assertTrue(self.reply_match("\d{2,3}", pinga.get_ttl()))

        self.assertTrue(self.reply_match("\d{2,3}.\d{2,3}", pinga.get_response()))

        self.assertTrue(self.reply_match("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", pinga.get_time() ))

        self.assertTrue(self.reply_match("\w+.\w+", pinga.get_dest() ))

    def test_fail_ftp_sunet(self):
        pinga = Ping('ftp.sunet.com')       

        print pinga.get_ttl()
        self.assertTrue(self.reply_match("0", pinga.get_ttl()))

        pinga.get_response()
        self.assertTrue(self.reply_match("\d{1,3}.\d{1,3}", pinga.get_response()))

        self.assertTrue(self.reply_match("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", pinga.get_time() ))

        self.assertTrue(self.reply_match("\w+.\w+", pinga.get_dest() ))


    def reply_match(self, pattern, match):
        if re.match(pattern, match) == None:
            return False
        return True

if __name__ == '__main__':
    unittest.main()

