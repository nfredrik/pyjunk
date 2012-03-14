import os
import sys

def main():

    args = sys.argv[1:]

    if not args or len(args) != 2:
        print 'usage: <pco-dir> <info-dir> '
        sys.exit(1)

    pco_root = args[0]
    info_root = args[1]

    pco_files = []
    for dirpath, dirnames, filenames in os.walk(pco_root):
       for filename in filenames:
           if filename.endswith('py'):
               pco_files.append(dirpath + '/' + filename)


    for pco_file in pco_files:
        print os.path.splitext(os.path.basename(pco_file))
        print os.path.splitext(os.path.basename(pco_file))[0]


    print 'the info files will be stored here:', info_root

if __name__ == '__main__':
  main()
