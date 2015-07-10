from collections import namedtuple

Test = namedtuple('Test', 'olle pelle')


print(Test)
#print(vars(Test))

l = [Test(olle=12, pelle=14), Test(olle=1, pelle=67)]

print(l)

for i in l:
	print(i)

for olle, pelle in l:
	print(olle, pelle)

