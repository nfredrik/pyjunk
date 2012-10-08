#!/usr/bin/env python
import pickle
import sys
import os

FILE='cobolmodules.pkl'

def read_dict_from_file():

    if not os.path.exists(FILE):
        return {}

    pkl_file = open(FILE, 'rb')
    the_dict = pickle.load(pkl_file)
    pkl_file.close()
    return the_dict



def main(args):

    args = args[1:]

    all = read_dict_from_file()
    #print all
    if args[0] in all:
        print args[0], all[args[0]]
    else:
        print 'Module:', args[0], 'not defined'
        return 42


if __name__ == '__main__':
  sys.exit(main(sys.argv))









