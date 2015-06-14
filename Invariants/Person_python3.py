from invariants import EnforceCheckRep

class Person(metaclass=EnforceCheckRep):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def incAge(self):
    self.age += 1

  def __privDecAge(self): # private method, won't be wrapped in a checkRep() call
    self.age -= 1


  def checkRep(self):
    print('checkRep()')
    assert 0 <= self.age < 100, 'not within bounds'
    assert type(self.name) is str, 'not a string'
    
if __name__ == '__main__':
    
    # valid input
    p =Person('nisse',99)
    #p.incAge()
    
    p = Person('janne',99)
    
    p = Person('olle', 34)