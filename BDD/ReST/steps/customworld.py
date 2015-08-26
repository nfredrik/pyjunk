
import datetime
from dateutil import parser

import json
import requests
import collections
from collections import namedtuple
from hamcrest import assert_that, contains_string, equal_to, is_not, not_none, less_than, less_than_or_equal_to 

resource_type = collections.namedtuple('resource_type', 'path')
mime_type = collections.namedtuple('mime_type', 'typ value')
payload = collections.namedtuple('payload', 'title body userId')
submap  = collections.namedtuple('submap', 'res number')

class CustomWorld(object):
    def __init__(self, host ='http://jsonplaceholder.typicode.com', port='80'):
        self.resources = dict()
        self.payload = None
        self.payloads = dict()
        #self.sub_map = list()
        self.sub_map = None
        self.host = host
        self.port = port
        self.mimes = dict()

    def set_resources(self, table):
        for row in table:
            self.resources[row["type"]] = row["path"]

    def set_mime_types(self, table):
        for row in table:
           self.mimes[row["type"]] = mime_type(typ= row['type'], value = row['path'])            

    def set_payloads(self, table):
        for row in table:
            self.payloads[row["payload"]] = payload(title= row['title'], body = row['body'], userId= row['userId'])

    def set_payload(self, id):
        self.payload = id

    def set_resource_type(self, res):
        self.resource = res

    def set_substitution(self, res, number):
        self.sub_map = submap(res = res, number = number)

    def substitute(self):
        if self.sub_map:
            if self.sub_map.res in self.resources[self.resource]:
                self.resources[self.resource] = self.resources[self.resource].replace(self.sub_map.res, self.sub_map.number)


    def request_resource(self, mime=None):

        # Subsitute all e.g. /posts/{id}  with /posts/1
        self.substitute()

        if not mime:
            self.response = requests.get(self.host + self.resources[self.resource])
        else:
            tmp = {'Content-Type':mime}
            self.response = requests.get(self.host + self.resources[self.resource], headers= tmp)

        return self.response

    def request_resource_ng(self, mime=None):
        name = self.the_link
        self.response = requests.get(name)

        return self.response

    def create_resource(self, format = 'json'):

        if format == 'json':
            data = dict()
            for name in self.payloads[self.payload]._fields:
                data[name] = getattr(self.payloads[self.payload],name)
            payload = json.dumps(data)
        else:
            pass # Handle html e.g.

        self.response = requests.post(self.host + self.resources[self.resource], payload)
        return self.response

    def supported_methods(self):
        self.response = requests.options(self.host)

    def check_for_existence(self):
        self.substitute()
        self.response = requests.head(self.host + self.resources[self.resource])

    def delete_resource(self):
        self.substitute()
        self.response = requests.delete(self.host + self.resources[self.resource])

    def assert_response(self, code):
        assert_that(self.response.status_code, equal_to(code))

    def assert_have_content(self):
        assert_that(self.response.content, is_not(equal_to(None)))

    def valid_json(self, dict):
        try:
            json.loads(text)
            return True
        except:
            return False

    def assert_valid_payload(self):
        #assert_that(isinstance(self.response.json, dict), equal_to(True))
        print(self.response.json)
        #assert self.valid_json(self.response.json)

    def assert_supported_methods(self, a_set):
        self.methods = set(self.response.headers['access-control-allow-methods'].split(','))
        print(self.methods)
        assert_that(a_set.issubset(self.methods))

    def assert_valid_metadata(self):
        actual_time = parser.parse(self.response.headers['Date'])
        assert_that(actual_time, less_than_or_equal_to(datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)))
        
    def assert_mime_type(self, mime):
        assert_that(self.response.headers['Content-Type'], equal_to(self.mimes[mime].value)) 

    def assert_attribute(self, name):
        hit = False
        items = self.response.json()
        for key in items.keys():
           if name == key:
            hit = True
            self.the_link = items[name]

        hitta = any([bool(key) for key in items.keys() if name == key])
        
        assert_that(hit, equal_to(True))

    def assert_attribute_in_text(self, attr):
        assert_that(self.response.headers, contains_string(attr))


