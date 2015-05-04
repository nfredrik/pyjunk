import json
import re
import sys
import requests
from genericdb import GenDB
from datetime import datetime
from collections import namedtuple

''' Named tuple "class". Work almost as a struct in C.
    see http://rrees.me/2015/04/28/python-preferring-named-tuples-over-classes/
'''

OK, ERROR = 0, 1

''' Inherit Base class to be able to raise own defined exceptions '''
class DataError(Exception): pass

''' Type definition of a complex structure'''
Stock = namedtuple('Stock', 'name url value date')

def read_json(file):
	''' Open and read the full content of a json file '''
	try:
		with open(file) as f:
			f = f.read()
			data = json.loads(f)
		return data
	except Exception as e:
		raise DataError(e.__class__, sys.exc_info()[-1].tb_lineno, file)

def geturl(url=''):
	''' Fetch a request URL'''
	try:
		sock = requests.get(url)
		html = sock.text
		sock.close()
		return html
	except Exception as e:
		raise DataError(e.__class__, sys.exc_info()[-1].tb_lineno, url)


def senasteNAV(url=''):
	''' Filter out appropriate data from morningstar web page. Need to be 
	changed if morningstar
	changes format'''
	
	html = geturl(url)
	nav = re.search('Senaste NAV.*\ ([\d]*\,[\d]*)\ SEK[.]*', html)

	if nav is None:
		raise DataError(DataError, sys.exc_info()[-1].tb_lineno, url)

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

		''' Exceptions casued either input error OR problem with underlaying 
			infrastructure lik net or sqlite database Log and exit '''
	except FileNotFoundError as e:

		print ("File not found: {}, lineno:{}".format(e, sys.exc_info()[-1].tb_lineno))
		return ERROR

	except DataError as e:
		print("Error: Class, lineno and message: {}".format(e))

#	except sqlite.OperationError as e:  Better as DBException as e:
#		print ("Problem with sqlite")
		return ERROR

		""" Internal programming error. Collect and Log and exit
		"""
	except AssertionError as e:
		print ("Internal programming error. Log and exit:{}, lineno: {}".format(e, sys.exc_info()[-1].tb_lineno))
		return ERROR

if __name__ == '__main__':

	sys.exit(main(sys.argv[1:]))


'''TODO:
	- Follow EP14 concept, check it out
	- Make a proper logfile for all exceptions! both for input/infra-problem and
	  internal programming errors....
'''
