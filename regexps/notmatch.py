import re
#
#I'm looking for a regular expression that will match all strings EXCEPT those that contain
# a certain string within. Can someone help me construct it?

#For example, looking for all strings that do not have a, b, and c in them in that order.

#So
#abasfaf3 would match, whereas
#asasdfbasc would not

r = re.compile("(?!^.*a.*b.*c.*$)")
r.match("abc")
r.match("xxabcxx")
r.match("ab ")
r.match("abasfaf3")
r.match("asasdfbasc")
