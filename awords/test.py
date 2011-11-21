import re
import sys
import pickle
import os
#
#
#
#<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
#"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
#<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="sv" xmlns:fb="http://www.facebook.com/2008/fbml" >
#<head profile="http://www.w3.org/2005/10/profile">
#<title>

#<link rel="stylesheet" type="text/css" href="/template/ver1-0/css/generalcss.jsp?611eada" />
#<link rel="stylesheet" type="text/css" href="/template/ver1-0/wireframe/normal/wireframecss.jsp?611eada" />
#<link rel="stylesheet" type="text/css" href="/template/ver1-0/wireframe/normal/variations/nyheter/nyheterCssV2.jsp?611eada" />
#<meta name="robots" content="noarchive" />
#<meta name="date" content="2011-11-13 22:59:40 +0100" />



def write_dict_2_file(dict):
    output = open('myfile.pkl', 'wb')
    pickle.dump(dict, output)
    output.close()

def read_dict_from_file():

    if not os.path.exists('myfile.pkl'):
        return {}

    pkl_file = open('myfile.pkl', 'rb')
    the_dict = pickle.load(pkl_file)
    pkl_file.close()
    return the_dict



def extract_date(filename):
    """
    Extract date from aftonbladet web site and as a string
    """
    fh = open(filename, 'r')
    the_whole = fh.read()
    date = re.findall('name="date" content="(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', the_whole)
    print date
    fh.close()



def extract_words(hash, filename):
    """
    Extract words in filename and add dictionary and sort
    """
    fh = open(filename, 'r')
    the_whole = fh.read()
    words = re.findall('[a-zA-Z]+', the_whole)
#    print words
    for word in words:
        if word not in hash:
            hash[word] = 1
        else:
            hash[word]+=1

    return hash

    for w in sorted(hash, key=hash.get, reverse=True):
        print w, hash[w]



    sys.exit(42)
    itemse = hash.items()
    itemse.sort()
    print itemse
    return
    print itemse
#    for key, value in itemse.items():
#        print key, value

    fh.close()




# Read dictionary file, what decides if there is something to read?
fredde = read_dict_from_file()

# Update with new information in dictionary
extract_words(fredde, 'a.html')

for w in sorted(fredde, key=fredde.get, reverse=True):
    print w, fredde[w]



# Store back ...
write_dict_2_file(fredde)

sys.exit(42)




fh = open('a.html', 'r')

for line in fh:
    print line
