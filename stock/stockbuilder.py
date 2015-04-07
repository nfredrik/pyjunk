import json
from dictionary import dict
from morningstar import Morningstar

class stockBuilder(object):
	def __init__(self, jsonf):
		self.stocks = []
		with open(jsonf) as data_file:
			json_file = data_file.read()
			self.data = json.loads(json_file)
	def build_stocks(self):
		for i, _ in enumerate(range(len(self.data["stocks"]))):
			stock = self.data["stocks"][i]
			#print ("type of stokc", stock.values())
			#print ("type of stokc", type(stock))
			self.stocks.append(Morningstar(stock))
		return self.stocks
