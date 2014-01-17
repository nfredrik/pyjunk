import sys


class Tests:
    tEsts = []
def moreTests():
    return None

def runNextTest():
    pass

def testName():
    pass
    
log = open('testlog', 'a')

def testdriver():
    while moreTests():
        try:
            runNextTest()
        except:
            log.write('FAILED', testName(), sys.exc_info())
        else:
            log.write('PASSED', testName())