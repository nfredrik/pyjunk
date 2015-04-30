import json
import re
import requests
from genericdb import GenDB
from datetime import datetime
from collections import namedtuple

''' Named tuple "class". Work almost as a struct in C.
    see http://rrees.me/2015/04/28/python-preferring-named-tuples-over-classes/
'''
Stock = namedtuple('Stock', 'name url value date')

def read_json(file):
	''' Open and read the full content of a json file '''
	with open(file) as f:
		f = f.read()
		data = json.loads(f)
	return data

def geturl(url=''):
	''' Fetch a request URL'''
	sock = requests.get(url)
	html = sock.text
	sock.close()
	return html

def senasteNAV(url=''):
	''' Filter out appropriate data from morningstar web page. Need to be 
	changed if morningstar
	changes format'''
	
	html = geturl(url)
	nav = re.search('Senaste NAV.*\ ([\d]*\,[\d]*)\ SEK[.]*', html)
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
			s = Stock(name=k, value=senasteNAV(v), url=v, date=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
		stocks.append(s)
	return stocks


''' Load json file with funds that interesting. It includes to URL to 
morningstars data about the fund
'''
test = build_stocks('./stocks.json')

''' Iterate over the collected data '''
for i in test:
	print (i.name, i.value, i.date)

''' Put the data in a sqlite database for later diagnostics'''


arrray = ["name text", "value text", "date text"]
db = GenDB('mystocks', fields= arrray)

for i in test:
	db.write([i.name, i.value, i.date])



