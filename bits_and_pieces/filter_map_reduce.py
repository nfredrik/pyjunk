def fille(x):
    return x % 2 != 0 and x %3 != 0


print filter(fille, range(2,25))



def cube(x):
   return x*x*x


print map(cube, range(1,11))


seq = range(8)

def add(x, y): return x +y

print map(add, seq, seq)


print reduce(add, range(1,11))
