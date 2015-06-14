import urllib.request
import json
import pprint
query_currencies = "https://api.coinbase.com/v1/currencies"

with urllib.request.urlopen( query_currencies) as document:
    #pprint.pprint(document.info().items())
#	currencies = json.loads( document.read().decode("utf-8"))
    currencies = json.loads(document.read().decode('utf8'))
    for i in currencies:
        try:
            print(i)
            pass
        except UnicodeEncodeError as e:
            print(e)    


