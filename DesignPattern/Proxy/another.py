class Implementation2:
    def f(self, param):
        print("Implementation.f()")
    def g(self):
        print("Implementation.g()")
    def h(self):
        print("Implementation.h()")

class Proxy2:
    def __init__(self, implementation= Implementation2()):
        self.__implementation = implementation
    def __getattr__(self, name):
        print 'hej'
        return getattr(self.__implementation, name)


if __name__ == '__main__':  
  p = Proxy2()
  p.f('params')
  
