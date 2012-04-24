import os
import sys
from command import Command
from pcoobject import PcoObject
from infoobject import InfoObject

def main():


    args = sys.argv[1:]

    if not args or len(args) != 2:
        print 'usage: <pco-dir> <info-dir> '
        sys.exit(1)


    if not os.path.exists(args[0]):
        print 'Did not find pco file dir'
        sys.exit(1)


    if not os.path.exists(args[1]):
        print 'Did not find info file directory'
        sys.exit(1)


    pco_root = args[0]
    info_root = args[1]

    pco_files = []

    # Build a list of pco objects
    for dirpath, dirnames, filenames in os.walk(pco_root):
       for filename in filenames:
           if filename.endswith('pco'):
               pco_files.append(PcoObject(dirpath + '/' + filename, dirpath.strip('.')))
               
               if os.path.splitext(filename)[0] != pco_files[-1].get_program_id():
                   print 'filename:', os.path.splitext(filename)[0],  'and program-id:' , pco_files[-1].get_program_id(), 'differs'
                   
    if len(pco_files) == 0:
        print 'No files to treat!'
        sys.exit(42) 

    # Iterate and generate an info file for every pco file
    for pco_object in pco_files:

        # Get copypaths
        proc = pco_object.get_uniq_copys()

        # Create a info object and add copypaths
        info_object = InfoObject(pco_object.get_filename(),
                                 info_root + '/'+  pco_object.get_filename(),
                                 pco_object.get_filepath(), [k  for k in proc.iterkeys() ])    


        # Populate info file with copys and includes
        for (mod, proc) in pco_object.get_copys():
            info_object.add_copys(proc, mod)

        for include in pco_object.get_sql_include():
            info_object.add_sql_includes(include)

if __name__ == '__main__':
    main()

