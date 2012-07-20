# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.

def luhn_algo(list, even):

    cntr = 0
    tsum = 0

    print list 
    for i in reversed(list):
        if cntr % 2 != even:
            tmp = int(i) * 2
            if tmp > 9:
                tmp = tmp - 9
            tsum+=tmp
        else:
            tsum+=int(i)

        cntr+=1

    if tsum % 10 == 0:
        return True

    return False


def is_luhn_valid(n):

    count = len(str(n))
    str_int_list = list(str(n))

    if count % 2 == 0:
        return luhn_algo(str_int_list, 0)
    else :
        return luhn_algo(str_int_list, 1)




if is_luhn_valid(1234):
    print 'yes valid'
else :
    print 'no unvalid'    