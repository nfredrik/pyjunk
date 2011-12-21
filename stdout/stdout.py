import sys
sys.stdout = open("test.txt", 'a')
print "Hello World!"
print "This is a test!"
sys.stdout = sys.__stdout__  # restore stdout back to normal
print "Hello World!"
