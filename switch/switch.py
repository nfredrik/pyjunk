
def fun1():
    print "fun1"
    
def fun2():
    print "fun2"
    
def default():
    print "default"
    
    
mydict = {1:fun1, 2:fun2}


my_func = mydict.get(1,default)
my_func()


my_func = mydict.get(3,default)
my_func()