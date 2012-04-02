class Person(object):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person:%s, %s]' % (self.name, self.pay)


class Manager(Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


class CManager(object):
    """
    Composition
    """
    def __init__(self, name, pay,  person=None):
        
        self.person = person or Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(self, percent + bonus)

    def lastName(self):
        return self.person.lastName()

    def __getattr__(self, attr):
        return getattr(self, attr)

    def __str__(self):
        return str(self.person)



if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job ='dev', pay = 100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 500000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)


    fred = CManager('Fredrik Svard', 50000000)
    print(fred.lastName())
    print(fred)

    from mock import Mock

    mockPerson = Mock()
    mockPerson.lastName.return_value = 'Larsson'
    mockPerson.__str__.return_value = 'PelleStina'


    john = CManager('Fredrik Svard', 50000000, person=mockPerson)
    print(john.lastName())    
    #print(john) 
