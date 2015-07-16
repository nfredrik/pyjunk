
# http://httpstatus.es/

class NamedHTTPstatus(object):
    """Map named HTTPstatuses into numbers."""
    MAP= {
       "OK": 200,
       "CREATED": 201,
       "NO_CONTENT": 204,
       "NOT_MODIFIED": 304,
       "BAD_REQUEST": 400,
       "UNAUTHORIZED": 401,
       "FORBIDDEB": 403,
       "METHOD_NOT_ALLOWED": 405,
       "CONFLICT" : 409,
       "INTERNAL_SERVER_ERROR": 500,        
    }

    @classmethod
    def from_string(cls, named_number):
#        name = named_number.strip().lower()
        name = named_number.strip()
        return cls.MAP[name]
