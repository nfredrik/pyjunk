print all([True, True, True, False, True, True])
print any([True, True, True, False, True, True])


import inspect

def getLineNumber():
    return inspect.currentframe().f_back.f_lineno

print "This",getLineNumber()
print "is just",getLineNumber()
pass
print "a test",getLineNumber()