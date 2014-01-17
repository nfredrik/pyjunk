# 
# Modify `remove_html_markup` so that it actually works!
#

def remove_html_markup(s):
    tag   = False
    quote = False
    out   = ""
    print 'token, tag, quote'
    for c in s:
        print c, tag, quote
        if c == '<' and not quote:
            tag = True
#        elif c == '>' and not quote:
        elif c == '>':
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c
            quote = False

    return out


def test():
    print remove_html_markup('<a href="don' + "'" + 't!">Link</a>')
    #assert remove_html_markup('<a href="don' + "'" + 't!">Link</a>') == "Link"


test()