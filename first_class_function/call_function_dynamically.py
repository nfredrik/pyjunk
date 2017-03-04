
def ett():
    print 'ett'


def tva():
    print 'tva'

    
def tre():
    ett()
    tva()

lista = [ett, tva, tre]


for i in lista:
    i()
