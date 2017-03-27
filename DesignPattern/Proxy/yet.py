import json


class Implementation2:
    def foo(self, param):
        print("Implementation.f()")
    def g(self):
        print("Implementation.g()")
    def h(self):
        print("Implementation.h()")

class Proxy3:
    def __init__(self, implementation= Implementation2(), recfile='trettio.json'):
        self.__implementation = implementation
        self.__recfile = recfile
        self.__fh = open(recfile, 'w')
        
    def foo(self, param):
        self.__fh.write(param)
        self.__implementation.foo(param)

    def __del__(self):
        self.__fh.close()


if __name__ == '__main__':  
  p = Proxy3()
  p.foo('params')
  
