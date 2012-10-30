#!/usr/bin/env python
import pickle
import sys
import os

FILE='cobolmodules.pkl'

def read_dict_from_file(file):

    if not os.path.exists(file):
        return {}

    pkl_file = open(file, 'rb')
    the_dict = pickle.load(pkl_file)
    pkl_file.close()
    return the_dict



def main(args):

    args = args[1:]

    all = read_dict_from_file(args[0])
    #print all
    if args[1] in all:
#        print args[1], all[args[1]]
        print all[args[1]]
        return all[args[1]]
    else:
        print 'Module:', args[1], 'not defined'
        return 42

#    print all


if __name__ == '__main__':
  sys.exit(main(sys.argv))









