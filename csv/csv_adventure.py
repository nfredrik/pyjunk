from hamcrest import assert_that, contains_string, equal_to, is_not
import csv


def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m

class Nuda(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "{}({!r},{!r})".format(self.__class__.__name__, self.x, self.y)

    def sum(self):
        return self.x + self.y

    def __eq__(self, other):
    	pass
    	return True


nuda = Nuda(3, 4)
dada = Nuda(4, 5)

print(nuda.sum())
#D  = get_class("Nuda(5, 6)")
#print(D.sum())

print(type(eval(repr(nuda))))
print(type(nuda))

assert_that(eval(repr(nuda)), equal_to(nuda))

ll = [nuda, dada]

with open('my.csv', 'w') as fh:
    #writer = csv.writer(fh, delimiter="\n")
    for l in ll:
    	#writer.writerow(str(l))
    	fh.write(str(l) + '\n')


with open('my.csv', 'r') as fh:
    n = fh.read()
    nn = eval(n)
    print('#', n.sum())
