import sys
from testtools import TestCase

def test_response_has_bold():
   # The response has bold text.
   response = self.server.getResponse()
   self.assertThat(response, HTMLContains(Tag('bold', 'b')))
   
   
def main(args):
     pass  
   
   
   
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
