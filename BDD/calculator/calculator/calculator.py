from .invariants import EnforceCheckRep

class Calculator(metaclass=EnforceCheckRep):
    number_types = (int, float, complex)

    def __init__(self):
        self.x, self.y = 0, 0

    def add(self, x, y):
        self.x, self.y = x, y
        return self.x + self.y

    def new_add(self, x, y):

        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
           return x + y
        else:
            raise ValueError("Wrong type:{}".format(type(x)))

    def checkRep(self):
        assert isinstance(self.x, self.number_types)