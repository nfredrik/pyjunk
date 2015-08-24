
import json
import requests
import collections
from collections import namedtuple
from hamcrest import assert_that, contains_string, equal_to, is_not

resource_type = collections.namedtuple('resource_type', 'path')
mime_type = collections.namedtuple('mime_type', 'typ value')
payload = collections.namedtuple('payload', 'title body userId')
submap  = collections.namedtuple('submap', 'res number')

class CustomWorld(object):
    def __init__(self, host ='http://jsonplaceholder.typicode.com', port='80'):
        self.resources = dict()
        self.payload = None
        self.payloads = dict()
        self.sub_map = list()
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
        self.sub_map = map
        self.sub_map = submap(res = res, number = number)

    def substitute(self):
        print(self.sub_map)
        if self.sub_map:
            if self.sub_map.res in self.resources[self.resource]:
                self.resources[self.resource] = self.resources[self.resource].replace(self.sub_map.res, self.sub_map.number)


    def request_resource(self, mime=None):
        url = self.host

        if self.sub_map:
            if self.sub_map.res in self.resources[self.resource]:
                self.resources[self.resource] = self.resources[self.resource].replace(self.sub_map.res, self.sub_map.number)

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

        url = self.host

        self.response = requests.post(self.host + self.resources[self.resource], payload)
        return self.response

    def delete_resource(self):
        self.substitute()
        print(self.host + self.resources[self.resource])
        self.response = requests.delete(self.host + self.resources[self.resource])


    def assert_response(self, code):
        assert_that(self.response.status_code, equal_to(code))

    def assert_have_content(self):
        assert_that(self.response.content, is_not(equal_to(None)))

    def assert_mime_type(self, mime):
        assert_that(self.response.headers['Content-Type'], equal_to(self.mimes[mime].value)) 

    def assert_attribute(self, name):
        hit = False
        items = self.response.json()
        for key in items.keys():
           if name == key:
            hit = True
            self.the_link = items[name]
        
        assert_that(hit, equal_to(True))

    def assert_attribute_in_text(self, attr):
        #print(self.response.content)
        assert_that(self.response.headers, contains_string(attr))


