import sys

# default
def f(a, b=2, c=3): print a, b, c

# arbitrary args
def func(*args): print args

# arbitrary args, keywords
def funck(**args): print args

# all
def funcka(a, *pargs, **kargs): print a, pargs, kargs

def  main(args):
    
    f(1)
    
    func(1,8,16,32)
    
    funck(a=5, b=34)
    
    funcka(1,2,3,x=1, y=2)
    return 0






if __name__ == '__main__':
  sys.exit(main(sys.argv))