from savejson import load_json

JSONFILE='test.json'


data = load_json(JSONFILE)

print data

for i in data:
    for l in i.keys():
        print l, i[l]