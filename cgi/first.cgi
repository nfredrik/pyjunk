#!/usr/bin/python 
# Tell the browser how to render the text 
print "Content-Type: text/plain\n\n"
#print "Hello, Python!" # print a test string 
template = "<html><body><h1>Hello %s!</h1></body></html>"
print template % "Reader"
