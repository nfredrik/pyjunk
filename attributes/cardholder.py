# File validate_getattr.py

class CardHolder:
    acctlen = 8                                  # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __setattr__ too
        self.age  = age                          # _acct not mangled: name tested
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    def __getattr__(self, name):
        if name == 'acct':                           # On undefined attr fetches
#            return self._acct[:-3] + '***'           # name, age, addr are defined
            return self._acct[:-3] + '***'           # name, age, addr are defined
        elif name == 'remain':
            return self.retireage - self.age         # Doesn't trigger __getattr__
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name':                           # On all attr assignments
            value = value.lower().replace(' ', '_')  # addr stored directly
        elif name == 'age':                          # acct mangled to _acct
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name  = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value                  # Avoid looping (or via object)

def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr)


if __name__ == '__main__':
    #CardHolder = loadclass()
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    printholder(bob)
    bob.name = 'Bob Q. Smith'
    bob.age  = 50
    bob.acct = '23-45-67-89'
    printholder(bob)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    printholder(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')

    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')


    try:
        sue.addr = '125 main st'
    except:
        print ('Bad addr for sue')
    else:
        print sue.addr
        print ('Ok addr for sue')    