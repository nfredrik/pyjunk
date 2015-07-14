import unittest
import json
import validictory
import pprint
import requests
from jsonplaceholder import REST

BASE_URL='http://jsonplaceholder.typicode.com'




def is_valid_json(text):
    try:
        json.loads(text)
        return True
    except:
        return False

# http://jsonschema.net/#/

def validate_json(text):

    schema = {"type": "object"}
    oldschema ={
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://jsonschema.net",
    "type": "object",
    "properties": {
    "body": {
      "id": "http://jsonschema.net/body",
      "type": "string"
    },
    "id": {
      "id": "http://jsonschema.net/id",
      "type": "integer"
    },
    "userId": {
      "id": "http://jsonschema.net/userId",
      "type": "integer"
    },
    "title": {
      "id": "http://jsonschema.net/title",
      "type": "string"
    }
    },
    "required": [
    "body",
    "id",
    "userId",
    "title"
    ]
    }
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(text)
    nisse = json.dumps(text)
    #pp.pprint(data)
    #print(data)
    #schema = {"type":"object"}

    schema = {



    "userId": {
      "type": "string"
    },

    "id": {
      "type": "integer"
    }
     ,
    "body": {
      "type": "string"
    }
   , 
   "titl": {
      "type": "string"
    },
       "required": [
    "body",
    "id",
    "userId",
    "titl"
    ]
    
    }


    #schema = {"type":"object","properties":
    #{"id":{"type":"integer"}, "title":{"type":"string"}, "body":{"type":"string"}, "userid":{"type":"integer"}}}
    validictory.validate(nisse, schema)

class restingTests(unittest.TestCase):
    def setUp(self):
        self.rest = REST()

    def assert_valid_dict(self, dict):
        for key in ['id', 'body', 'title', 'userId']:
            if key not in dict.keys():
                raise self.failureException("%s not in dict"%key)

            if dict[key] is None:
                raise self.failureException("no value for %s"%key)

        validate_json(str(dict))

    def assert_valid_list(self, list):
        for dict in list:
            self.assert_valid_dict(dict)

    def test_list_primitives(self):
        prim = self.rest.show_primitives().options()
        ll = set(prim.split(','))
        at_least = set(['PUT', 'GET'])
        self.assertTrue(at_least.issubset(ll))      

    def test_url_show_resource(self):
        url = self.rest.show_resource(number='1').url
        self.assertEqual(BASE_URL+'/posts/1', url)

    def test_show_resource(self):
        j = self.rest.show_resource(number='1').json
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(j)
        k = json.dumps(j)
        #pp.pprint(k)
        # Verify valid json
        self.assertTrue(isinstance(j,dict))
        self.assert_valid_dict(j)


    def test_url_list_resources(self):
        url = self.rest.list_resources().url
        self.assertEqual(BASE_URL+'/posts', url)

    def test_list_resources(self):
        j = self.rest.list_resources().json
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(j)
        self.assertTrue(isinstance(j,list))
        self.assert_valid_list(j)

    def test_url_create_resource(self):
        data1 = {"title":"foo", "body":"bar", "userId":"1"}
        data = json.dumps(data1)
        j, text = self.rest.create_resource().create(data)
        expect = {"id":101, "title":"foo", "body":"bar", "userId":1}
        text = json.loads(text)

        self.assertTrue(j.status_code == requests.codes.ok)

        self.assertEqual(expect, text)

    def test_url_update_resource(self):

        data1 = {'title':'foo', 'body':'bar', 'userId':'1'}
        data = json.dumps(data1)     
        j, text = self.rest.update_resource(number='1').update(data)
        expect = {"id":1, "title":'foo', "body":'bar', "userId":1}
        text = json.loads(text)

        self.assertTrue(j.status_code == requests.codes.ok)
        self.assertEqual(expect, text)


    def test_delete_resource(self):
        r = self.rest.delete_resource(number='1').delete()

        #Delete should return 204 instead of 200, weird??

        self.assertTrue(r.status_code == requests.codes.ok)


    # def test_filtering_resources(self):
    #     text = self.rest.filtering_resources(from_='Bob').text
    #     self.assertEqual('rest you very much. - Bob', text)

    # def test_nested_resources(self):
    #     text = self.rest.nested_resources(from_='Bob').text
    #     self.assertEqual('rest you very much. - Bob', text)


if __name__ == '__main__':
    unittest.main()
