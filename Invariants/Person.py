import types

def public(func):
  def wrapper(self,*__args,**__kw):
    self.checkRep() # check before executing
    res = func(self,*__args,**__kw)
    self.checkRep() # check after executing
    return res
  return wrapper

def constructor(func):
  def wrapper(self,*__args,**__kw):
    func(self,*__args,**__kw)
    self.checkRep() # check after executing constructor
  return wrapper

# Put "__metaclass__ = EnforceCheckRep" inside a class declaration to
# have it automatically decorate its constructor and public methods with
# checkRep() calls
def EnforceCheckRep(name, bases, attrs):
  for k in attrs:
    if k == '__init__':
      attrs[k] = constructor(attrs[k])
    # ignore private methods that start with '_' (and of course ignore checkRep itself)
    elif k[0] != '_' and k != 'checkRep':
      f = attrs[k]
      if isinstance(f, types.FunctionType):
        attrs[k] = public(f)
  return type(name, bases, attrs)
  

class Person:
  __metaclass__ = EnforceCheckRep # the ONLY line you need to add to the class definition

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def incAge(self):
    self.age += 1

  def __privDecAge(self): # private method, won't be wrapped in a checkRep() call
    self.age -= 1


  def checkRep(self):
    print 'checkRep()'
    assert 0 <= self.age < 100, 'not within bounds'
    assert type(self.name) is str, 'not a string'
    
if __name__ == '__main__':
    
    # valid input
    p =Person('nisse',99)
    #p.incAge()
    
    p = Person('janne',99)
    
    p = Person(334, 34)