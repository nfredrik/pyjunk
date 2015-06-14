import re, os

PATTERN = re.compile("[\d]{4}-[\d]{2}-[\d]{2}T[\d]{2}:[\d]{2}:[\d]{2}(.*)")


def has_posix(filename, pattern):

    print("checking%s"%filename)
    
    with open(filename) as fh:
        lines = fh.readlines()
        for line in lines:
            if pattern.search(line): return True

    return False


candidates  = [os.path.join(root, f)  for root, _, files in os.walk('.') for f in files if f.endswith('.log')]
posix = [ file for file in candidates if has_posix(file, PATTERN)]


print(posix)


# print('\n')
# print("Has posix timestamp")
# for p in posix:
# 	print(p)
