
import sys

def main(args):

  if not args:
    print 'usage: <file to count>'
    sys.exit(1)

  fh = open(args[0], 'r')
  string = fh.read()


  dict = {}
  for line in string.split():
#      print line
      for words in line.split():
#          print words
          for token in words.split():
              print token
              if token not in dict:
                  dict[token] = 1
              else:
                  dict[token] += 1

print dict

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
