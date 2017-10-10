import json

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}


# Writing JSON data
with open('data.json', 'w') as f:
     json.dump(data, f)


# Reading data back
with open('data.json', 'r') as f:
     data1 = json.load(f)

data1['natti'] = {'mera': 4555}     

print(data1)   

with open('data.json', 'w') as f:
     json.dump(data1, f)
