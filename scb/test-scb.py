post ="""{   
"query": [
 {       
 "code": "ContentsCode",
  "selection": {         
    "filter": "item",         
    "values": [           
      "BE0101N1"         
    ]       
   }     
},    
{       
  "code": "Tid",
   "selection": {         
   "filter": "item",         
   "values": [           
   "2010",           
   "2011"         
   ]       
  }     
 }    
],   
"response": {     
  "format": "json"   
 } 
}"""


import requests


r = requests.post("http://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0101/BE0101A/BefolkningNy", data=post)
#r.text.encode('utf-8-sig')
#print (r.text)
#print (r.status_code)
r.encoding = 'utf-8-sig'

#print (r.headers['content-type'])
#print (r.content)
#print('r.text type{}'.format(type(r.text)))
#print (r.text)
#print (r.text.decode('utf-8-sig'))
print(r.json())