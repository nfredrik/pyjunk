
import requests
JSONPLACEHOLDER='jsonplaceholder.typicode.com'
from steps.jsonplaceholder import REST_light, RESTingResponse
from hamcrest import assert_that, contains_string, equal_to, is_not

resources = dict()

class CustomWorld(object):
    def __init__(self):
        self.resources = dict()
        self.sub_map = list()
        self.response = RESTingResponse(url='')
        self.host = 'http://jsonplaceholder.typicode.com'
        self.port = '80'

    def set_resources(self, table):
        for row in table:
            self.resources[row["type"]] = row["path"]

    def set_mime_types(self, table):
        for row in table:
            self.resources[row["HTML"]] = row["text/html"]

    def set_resource_type(self, res):
        self.resource = res

    def set_substitution(self, map):
        self.sub_map = map

    def request_resource(self):
        url = self.host

        if self.sub_map:
            if self.sub_map[0] in self.resources[self.resource]:
                self.resources[self.resource] = self.resources[self.resource].replace(self.sub_map[0], self.sub_map[1])

        self.response = REST_light(url=self.host+self.resources[self.resource])

        return requests.get(self.host + self.resources[self.resource])

    def assert_response(self, code):
        assert_that(self.response.status_code, equal_to(code))

    def assert_have_content(self):
        assert_that(self.response.has_content, equal_to(True))

