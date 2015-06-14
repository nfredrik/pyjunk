import re, os

# http://tech.pro/tutorial/1554/four-tricks-for-comprehensions-in-python



pattern = re.compile("[\d]{4}-[\d]{2}-[\d]{2}T[\d]{2}:[\d]{2}:[\d]{2}(.*)")


def has_posix(filename, pat):

    print("checking%s"%filename)
    
    with open(filename) as fh:
        lines = fh.readlines()
        for line in lines:
            if pat.search(line): return True

    return False

def matching(pattern, line):
    print(line)
    if pattern.search(line):
        raise StopIteration


def stop():
    raise StopIteration

def stopif(expr):
    if expr:
        raise StopIteration
    return True


#text = "My hovercraft is full of eels."
text = " I can't tell the difference between Whizzo butter and this dead crab."
first_chars = []

#first_chars = [word[0] if word != "and" else stop() for word in text.split()]
first_chars = list(word[0] for word in text.split() if stopif(word == "and"))
#first_chars = list(word[0] if word != "and" else stop() for word in text.split())

#print(first_chars)

#fine = [True for line in open('myfile.log').readlines() if pattern.search(line) ]

#print(fine)

candidates  = [os.path.join(root, f)  for root, _, files in os.walk('.') for f in files if f.endswith('.log')]

#posix = [ file for file in candidates if has_posix(file, pattern)]
posix = set([file for file in candidates for line in open(file).readlines() if pattern.search(line)])
#posix = list(file for file in candidates for line in open(file).readlines() if stopif(pattern.search(line)))
#if pattern.search(line)
#posix = [ file for file in candidates  if not pattern.search(line) else stop() for line in open(file).readlines() ] 

#first_chars = [file if pattern.search(line) is None else stop() for file in file in candidates for line in open(file).readlines()]

all = set(candidates)

# s -= t    return set s after removing elements found in posix
all.difference_update(posix)

#print(all)

for n in all:
    print(n)
#print(posix)


#print('\n')
# print("Has posix timestamp")
# for p in posix:
# 	print(p)
