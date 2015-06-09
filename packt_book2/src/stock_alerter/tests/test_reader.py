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

	def assert_has_correct_syntax(self, entry):
		""" Verify that we have a string, datetime-type object and  valid digits """

		if re.match("[\w]*", entry[0]) is None:
			raise self.failureException("Wrong symbol: {}".format(entry[0]))

		if not isinstance(entry[1], datetime):
			raise self.failureException("Wrong symbol: {}".format(entry[0]))

		if re.match("[\d]*", str(entry[2])) is None:
			raise self.failureException("Wrong symbol: {}".format(entry[2]))		


class HTTPReaderTest(HTTPReaderSyntaxTest):

	# def testHTTPReader_returns_valid_format1(self):
	# 	reader = HTTPReader(["GOOG"])
	# 	updater = reader.get_updates()
	# 	update = next(updater)
	# 	self.assertEqual(("GOOG", datetime(2015, 5,29,20,0), 532), update)


	def testHTTPReader_returns_valid_format2(self):
		reader = HTTPReader(["GOOG"])
		updater = reader.get_updates()
		update = next(updater)
		self.assert_has_correct_syntax(update)
