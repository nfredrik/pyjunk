import sys

sys.stderr = sys.__stdout__  
print "Hello World!"
print "This is a test!"
sys.stdout = sys.__stdout__  # restore stdout back to normal
print "Hello World!"

sys.stderr = sys.__stderr__  
