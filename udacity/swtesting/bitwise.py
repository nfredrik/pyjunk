import random

def high_common_bits(a,b):
    mask = 0x8000000000000000
    output = 0
    for i in reversed(range(64)):
        if (a&mask) == (b&mask):
            output |= a&mask
        else:
            output |= mask
            return output
        mask >>= 1
    return output

def low_common_bits(a,b):
    mask = 1
    output = 0
    for i in range(64):
        if (a&mask) == (b&mask):
            output |= a&mask
        else:
            output |= mask
            return output
        mask >>= 1
    return output


def test(a,b):
    print "a=", a, "b=", b
    print high_common_bits(a,b)
    print low_common_bits(a,b)
    
    
for i in range(10000):
    a = random.getrandbits(64)
    b = a 
    # Turn b into a mutated input from a
    for j in range(random.randrange(63)):
        b ^= 1 << random.randrange(0,63)
        
    print high_common_bits(a,b) + low_common_bits(a,b)
    