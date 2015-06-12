import re

filter1 = re.compile("([\w\-\d\.\+]*\-[\d\.]+).*\.rpm")
filter2 = re.compile("([\w\-\d\.\+]*\-[\w\d\+]+).*\.rpm")

with open('rpms.txt') as fh:

	lines = fh.readlines()
	for row in lines:
		match = re.search(filter1, row) or re.search(filter2, row)
		if match is not None:
			pass
			#print (match.group(1),)
		else:
			#print ("NEJ!!!")
			print (row)

filter3 = re.compile("([\w\-\d\.\+]*\-[\w\d\+]+).*")
with open('xmu03.txt') as fh:
	lines = fh.readlines()
	for row in lines:
		match = re.search(filter3, row)

		if match is not None:
			print (match.group(1),)
