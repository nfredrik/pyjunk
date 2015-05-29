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

import re

class HTTPReaderSyntaxTest(unittest.TestCase):

	def validate_time(self, date_text):

		if type(date_text) is not datetime.date:
			raise self.failureException("Incorrect data format, should be YYYY-MM-DD")

		return

		try:
			datetime.strptime(date_text, '%Y-%m-%d')
		except ValueError:
			raise failureException("Incorrect data format, should be YYYY-MM-DD")

	def assert_has_correct_syntax(self, entry):
		pass

		if re.match("[\w]*", entry[0]) is None:
			raise self.failureException("Wrong symbol: {}".format(entry[0]))


# strftime('%m/%d/%Y')
		self.validate_time(entry[1])

		if re.match("[\d]*", str(entry[2])) is None:
			raise self.failureException("Wrong symbol: {}".format(entry[2]))		

class HTTPReaderTest(HTTPReaderSyntaxTest):
	def testHTTPReader_returns_valid_format(self):
		reader = HTTPReader(["GOOG"])
		updater = reader.get_updates()
		update = next(updater)
		self.assertEqual(("GOOG", datetime(2015, 5,28,20,0), 539), update)
		# TODO: Check for format/syntax...

		self.assert_has_correct_syntax(update)
