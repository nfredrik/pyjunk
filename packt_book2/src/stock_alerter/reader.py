import csv
from datetime import datetime

class ListReader:
	"""Reads a series of updates from a list"""
	def __init__(self, updates):
		self.updates = updates

	def get_updates(self):
		for update in self.updates:
			yield update

class FileReader:
	def __init__(self, filename):
		self.filename = filename

	def get_updates(self):
		"""Returns the next update everytime the method is called"""
		with open(self.filename, "r") as fp:
			data = fp.read()
			#lines1 = csv.reader(data)
			#print (lines1)
			lines = data.split()
			#print(lines)  
			for line in lines:
				#print(line.split(","))
				symbol, timestamp, price = line.split(",")
				yield(symbol,
					datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
					int(price))


from yahoo_finance import Share

class HTTPReader:
	"""Specify a list of stocks like GOOG, RHL etc to be read"""
	PRICE = 0
	TIME = 1

	def __init__(self, list):
		self.list = list
	"""Get list of current stock prices"""
	def get_updates(self):
		dict = {}
		r_list = []

		for symbol in self.list:
			try:
				s = Share(symbol)
				tmp = s.get_trade_datetime().split()
				timestamp = tmp[0]+'T'+tmp[1]+'.00'
				price = int(s.get_price().split(".")[self.PRICE])
				#print("type for price:{}".format(type(price)))
				dict[symbol] = [price, timestamp]
				del s 
			except:
				pass
				#print ("Could not find {} in yahoo finance".format(symbol))

		for item in dict:
			r_list.append((item, datetime.strptime(dict[item][self.TIME], "%Y-%m-%dT%H:%M:%S.%f"), dict[item][self.PRICE] ) )
#			r_list.append((item, datetime.now(), dict[item]))

		for i in r_list:
			yield i
			
		return ["GOOG", datetime(2104, 2, 13), 37]
