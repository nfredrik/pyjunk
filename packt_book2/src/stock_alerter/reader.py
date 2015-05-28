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
			lines = csv.reader(data) 
			for line in lines:
				symbol, timestamp, price = line
				yield(symbol,
					datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f)",
					int(price)))




class HTTPReader:
	"""Specify a list of stocks like GOOG, RHL etc to be read"""
	def __init__(self):
		pass
	"""Get list of current stock prices"""
	def get_updates(self):

		# Use 'requests' to fetch from relevant site

		return ["GOOG", datetime(2104, 2, 13), 37]
