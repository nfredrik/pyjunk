
class A(object):
    nisse = 15
    
    def __init__(self):
        jenne = 37
        self.roger = jenne
        
        
a = A()
b = A()
print 'a.nisse', a.nisse

#print a.jenne

print 'a.roger', a.roger

a.nisse =11
a.roger = 22

b.nisse = 00
b.roger = 66

print 'a.nisse', a.nisse

#print a.jenne

print 'a.roger', a.roger



