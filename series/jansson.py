import collections

number = [str(i) for i in range(0,10)] + [chr(i) for i in range(65,91)]
serie = ['AG{}'.format(n) for n in number]

print(serie)

log = collections.namedtuple('log', 'text logId')

nisse = log(text='hej hej', logId='AG0')

print(nisse)
