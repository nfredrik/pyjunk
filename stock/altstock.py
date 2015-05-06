import json
import re
import os
import sys
import requests
import logging
from dataerror import DataError
from genericdb import GenDB
from datetime import datetime
from collections import namedtuple

''' Named tuple "class". Work almost as a struct in C.
    see http://rrees.me/2015/04/28/python-preferring-named-tuples-over-classes/
'''

OK, ERROR = 0, 1

_log = logging.getLogger(' ')

''' Type definition of a complex structure'''
Stock = namedtuple('Stock', 'name url value date')

def read_json(file):
	''' Open and read the full content of a json file '''
	try:
		with open(file) as f:
			f = f.read()
			data = json.loads(f)
		
		return data

	except FileNotFoundError as e:
		raise DataError("Can not load json file: {}".format(e))

#	 	raise NDataError(message ="Cannot Load json file:{}".format(file),
#	 		             path = '...',
#	 		             line = sys.exc_info()[-1].tb_lineno)

def geturl(url=''):
	''' Fetch a request URL'''

	try:
		sock = requests.get(url)
		html = sock.text
		sock.close()
		return html
	except requests.exceptions.MissingSchema as e:
		raise DataError("Cannot fetch requested URL:{}".format(url))

def senasteNAV(url=''):
	''' Filter out appropriate data from morningstar web page. Need to be 
	changed if morningstar
	changes format'''
	
	html = geturl(url)
	nav = re.search('Senaste NAV.*\ ([\d]*\,[\d]*)\ SEK[.]*', html)

	if nav is None:
		raise DataError("Cannot find NAV in URL:{}".format(url))

	return nav.group(1).replace(",",".")

def build_stocks(file):
	''' Based on json file content fetch information and add list of
	Stocks
	'''
	stocks = []

	data = read_json(file)

	for i, _ in enumerate(range(len(data["stocks"]))):
		stock = data["stocks"][i]
		for k, v in stock.items():
			s = Stock(name=k, value=senasteNAV(v), url=v,
					 date=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
		stocks.append(s)
	
	return stocks

def main(args):

	exit_code = ERROR

	try:
		#assert False, "Putting assert False by purpose ...."

		''' Load json file with funds that is interesting. It includes URL to 
		morningstars data about the fund
		'''
		test = build_stocks('./stocks.json')

		''' Iterate over the collected data '''
		# for i in test:
		# 	print (i.name, i.value, i.date)

		''' Put the data in a sqlite database for later diagnostics'''


		arrray = ["name text", "value text", "date text"]
		db = GenDB('mystocks', fields= arrray)

		for i in test:
			db.write([i.name, i.value, i.date])

		exit_code = OK

	except (DataError, EnvironmentError) as error:
		''' Exceptions casued either input error OR problem with underlaying 
			infrastructure like net or sqlite database Log and exit.
			EnvironmentError embraces IOError, OSError 
		'''
		_log.error(error)

	except Exception as error:
		''' Programming error. Trace callback and line number in output 
		'''
		_log.exception(error)

	except :
		_log.exception("Fundamental problems:{}".format(sys.exc_info()[0]))

	return exit_code


if __name__ == '__main__':
	logging.basicConfig(level=logging.ERROR) # , filename='errors.log')
	sys.exit(main(sys.argv[1:]))

