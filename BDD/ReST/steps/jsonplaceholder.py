
#TODO
# Make it possible to use CLI for these features?
# Use BDD?
# Mocking by using sessions?
#
# Use jsonplaceholder
# use some available resources to play around with ...
# GET, POST, DELETE and do on to test
# Use click instead of OptionParser???

JSONPLACEHOLDER='jsonplaceholder.typicode.com'

import random
import requests
from optparse import OptionParser

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

class RESTingResponse(object):
    ''' Takes care of making the actual request'''
    def __init__(self, url, language=None):
        self.url = url
        self.language = language
        self.is_secure = url.startswith('https')
        self._html = None
        self._json = None
        self._text = None

    def _make_request(self, accept):
        return requests.get(self.url, headers={
            'Accept': accept,
            'Accept-Language': self.language or 'en-us'
        })

    def _post_request(self, accept):
        return requests.post(self.url, data=self.payload, headers={
            'Content-Type': 'application/json',
            'Accept-Language': self.language or 'en-us'
        })

    def _put_request(self, accept):
        return requests.put(self.url, data=self.payload, headers={
            'Content-Type': 'application/json',
            'Accept-Language': self.language or 'en-us'
        })

    def _patch_request(self, accept):
        return requests.patch(self.url, data=self.payload, headers={
            'Content-Type': 'application/json',
            'Accept-Language': self.language or 'en-us'
        })

    def _delete_request(self, accept):
        return requests.delete(self.url,  headers={
            'Content-Type': 'application/json',
            'Accept-Language': self.language or 'en-us'
        })

    def _options_request(self, accept):
        return requests.options(self.url,  headers={
            'Content-Type': 'application/json',
            'Accept-Language': self.language or 'en-us'
        })

    def _head_request(self, accept):
        return requests.head(self.url,  headers={
            'Content-Type': 'application/json',
            'Accept-Language': self.language or 'en-us'
        })

    @property
    def text(self):
        if self._text is None:
            self._text = self._make_request('text/plain')
        return self._text.text

    @property
    def json(self):
        if self._json is None:
            self._json = self._make_request('application/json')
        return self._json.json()

    @property
    def html(self):
        if self._html is None:
            self._html = self._make_request('text/html')
        return self._html.text

    def create(self, payload):
        if self._json is None:
            self.payload = payload
            self.r = self._post_request('application/json')
            #print (self.r, self.r.text)
        return self.r, self.r.text

    def update(self, payload):
        if self._json is None:
            self.payload = payload
            self.r = self._put_request('application/json')
        return self.r, self.r.text

    def patch(self, payload):
        if self._json is None:
            self.payload = payload
            self.r = self._patch_request('application/json')
        return self.r, self.r.text

    def options(self):
        self.r = self._options_request('application/json')
        hdr = self.r.headers['access-control-allow-methods']
        return hdr

    def head(self):
        self.r = self._head_request('application/json')
        time = self.r.headers['Date']
        return self.r, time

    def delete(self):
        if self._json is None:
            self.r = self._delete_request('application/json')
            print("NOTE!!!: from delete", self.r.ok, self.r.status_code, "should be 204!")
        return self.r

    @property
    def status_code(self):
        return 200


class REST_light(object):

    def __init__(self, url):
        self.url = url

    def __call__(self):
        def outer(path):
            def inner(secure=False, **kwargs):
                url = self.build_url(path, **kwargs)
                return RESTingResponse(url, language=self.language)
            return inner

        return outer(self.url) 


class REST(object):

    actions = {
        'show_resource':'posts/{number}',
        'list_resources': 'posts',
        'create_resource': 'posts',
        'update_resource': 'posts/{number}',
        'delete_resource': 'posts/{number}',
        'show_primitives':'',
        'patch_resource' :'posts/{number}',
        'head_resource'  :'posts/{number}'        
    }

    def __init__(self, secure=False, language=None):
        self.secure = secure
        self.language = language

    def __getattr__(self, attr):

        path = self.actions.get(attr)
        if path is None:
            raise AttributeError(attr)

        def outer(path):
            def inner(secure=False, **kwargs):
                url = self.build_url(path, **kwargs)
                return RESTingResponse(url, language=self.language)
            return inner

        return outer(self.actions[attr])

    def build_url(self, path, **kwargs):
        params = dict([(k, quote(v)) for k, v
            in kwargs.items() if v])
        url = '{protocol}://jsonplaceholder.typicode.com/{path}'.format(
            protocol='https' if self.secure else 'http',
            path=path.format(**params))
        #print("url:", url)
        return url        


rest = REST()

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option('-a', '--action', dest='action', default='off',
        help='Name of the action to perform')

    parser.add_option('-n', '--name', dest='name',
        help='Who do you want to REST off?')

    parser.add_option('-f', '--from', dest='from', help='Who are you?')

    parser.add_option('-c', '--company', dest='company',
        help='Which company do you want to REST off?')

    parser.add_option('-t', '--thing', dest='thing',
        help='What thing do you want to REST off?')

    parser.add_option('-r', '--reference', dest='reference',
        help='Who do you want to reference?')

    parser.add_option('-u', '--url', action='store_true', dest='url',
        help='Only display the URL (useful for c/ping)')

    (options, args) = parser.parse_args()

    options = vars(options)
    action = options.pop('action')
    url_only = options.pop('url')

    RESTing = getattr(REST, action)(**options)
    if url_only:
        print(RESTing.url)
    else:
        print(RESTing.text)
