#
# Finish the delta debug function ddmin
#


import re
import sys

counter = 0

def test(s):
    global counter
    counter+=1
    print counter, ':',
    s_merged = "".join(s)
    print s, len(s),
    if re.search("<SELECT[^>]*>", s_merged) >= 0:
        print 'FAIL'
        return "FAIL"
    else:
        print 'PASS'
        return "PASS"


def ddmin(s):
    assert test(s) == "FAIL"

    n = 2     # Initial granularity
    while len(s) >= 2:
        start = 0
        subset_length = len(s) / n
        some_complement_is_failing = False

        while start < len(s):
            complement = s[:start] + s[start + subset_length:]

            if test(complement) == "FAIL":
                s = complement
                n = max(n - 1, 2)
                print '1no subset:', n
                some_complement_is_failing = True
                #print 'NUDA'
                break
                
            start += subset_length

        if not some_complement_is_failing:
            # YOUR CODE HERE
           
            
            n = min(2*n, len(s))
            print '2no subset:', n
            #sys.exit(9)
            if n == len(s):
                break
            print 'POMG'

    return s

# UNCOMMENT TO TEST
#html_input = '<SELECT>foo</SELECT>'
html_input = ['<SELECT>', 'foo', '</SELECT>' ]
print ddmin(html_input)
print counter