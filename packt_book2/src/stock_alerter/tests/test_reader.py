import unittest
from unittest import mock
from datetime import datetime

from ..reader import FileReader # ListReader, HTTPReader
from ..reader import HTTPReader


class FileReaderTest(unittest.TestCase):
	@mock.patch("builtins.open",
				mock.mock_open(read_data="""
					                        GOOG,2014-02-11T14:10:22.13,5
											AAPL,2014-02-11T00:00:00.0,8
										 """))

	def test_FileReader_returns_the_file_content(self):
		reader = FileReader("stocks.txt")
		updater = reader.get_updates()
		update = next(updater)
		self.assertEqual(("GOOG", datetime(2014, 2,11,14,10, 22, 130000), 5), update)


class HTTPReaderTest(unittest.TestCase):
	def testHTTPReader_returns_valid_format(self):
		reader = HTTPReader(["GOOG"])
		updater = reader.get_updates()
		update = next(updater)
		self.assertEqual(("GOOG", datetime(2015, 5,28,20,0), 539), update)
		# TODO: Check for format/syntax...
