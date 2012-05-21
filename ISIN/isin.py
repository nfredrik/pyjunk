import re
 
def checkISIN(value):
    value = value.strip().upper()
    m = re.match('^([A-Z][A-Z])([A-Z0-9]{9}\d)$', value)
    if not m:
        return False
    sum_digits_str = ''.join(str(int(c, 36)) for c in value[:11])
    print sum_digits_str
    total_sum = 0
    parity = len(sum_digits_str) % 2
    print parity
    for n, c in enumerate(sum_digits_str):
        a = int(c)
        if n % 2 != parity:
            a = a * 2
        total_sum += a / 10
        total_sum += a % 10
    check_digit = (10 - (total_sum % 10)) % 10
    return value[11] == unicode(check_digit)
 
if __name__ == "__main__":
    for i in [
        'SE0002699421',  
        'SE0000428336',
        'US0378331005',
        'AU0000XVGZA3',
        'GB0002634946']:
        print i, checkISIN(i)
