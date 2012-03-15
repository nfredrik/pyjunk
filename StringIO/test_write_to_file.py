import unittest
from write_to_file import FileWrite
from StringIO import StringIO

class TestFileWrite(unittest.TestCase):
    def test___del__(self):
        # file_write = FileWrite()
        # self.assertEqual(expected, file_write.__del__())
        assert True # TODO: implement your test here

    def test___init__(self):
        # file_write = FileWrite()
        assert True # TODO: implement your test here

    def test_write_it(self):
        file_write = FileWrite()
        file_write.write_it('next.text', 'pelle olle')
        assert True # TODO: implement your test here

    def test_write_it_to_file(self):
        fh = StringIO()
        file_write = FileWrite()
        file_write.write_it_to_file(fh, 'foo bar')
        self.assertEqual('foo bar', fh.getvalue())

    def test_read_it(self):
        file_write = FileWrite()
        print file_write.read_it('next.text')
        assert True # TODO: implement your test here

    def test_read_it_from_file(self):
        fh = StringIO('olle bul')
        file_write = FileWrite()
        self.assertEqual('olle bull', file_write.read_it_from_file(fh))

if __name__ == '__main__':
    unittest.main()
