#!/usr/bin/env python
import sys
import re
import pickle

def write_dict_2_file(dict):
    output = open('cobolmodules.pkl', 'wb')
    pickle.dump(dict, output)
    output.close()


def main(args):
   
    args = args[1:]

#    with open('antcobolBuildtest', 'r') as fh:
    with open(args[0], 'r') as fh:
        data = fh.read().split('\n')

    all_pcos= {}

    for row in data:
        #    print row
        # <mfdirlist id="dirset.New_Configuration.WORKSPACE/src/pgm/PROD/FOBULB/FO9002.pco" refid="cobol_directive_set_1"/>
        gotit = re.search('\"dirset.New_Configuration\.([\/\w\d]+\/)([\w\d]+)\.pco\"',row)

        if gotit != None:
        #        print gotit.group(1), gotit.group(2)
            all_pcos[gotit.group(2)] = gotit.group(1)+gotit.group(2)+'.pco'
  

    #for key in all_pcos:
     #   print key, all_pcos[key]
    write_dict_2_file(all_pcos)



if __name__ == '__main__':
  sys.exit(main(sys.argv))
