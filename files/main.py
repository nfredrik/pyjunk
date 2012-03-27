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
    for dirpath, dirnames, filenames in os.walk(pco_root):
       for filename in filenames:
           if filename.endswith('pco'):
               pco_files.append(PcoObject(dirpath + '/' + filename, dirpath.strip('.')))
               
               if os.path.splitext(filename)[0] != pco_files[-1].get_filename():
                   print 'filename:', os.path.splitext(filename)[0],  'and program-id:' , pco_files[-1].get_filename(), 'differs'
                   sys.exit(42)

    if len(pco_files) == 0:
        print 'No files to treat!'
        sys.exit(42) 

    for pco_object in pco_files:

        # Get found copys in pco file
        copys = pco_object.get_copys()

        # Get copypaths, system copys, includes
        proc = pco_object.get_uniq_copys()
        system_copys = pco_object.get_copys_system()
        includes = pco_object.get_sql_include()

        # Create a info object and copypaths
        info_object = InfoObject(pco_object.get_filename(),
                                 info_root + '/'+  pco_object.get_filename(),
                                 pco_object.get_filepath(), [k  for k in proc.iterkeys() ])    

        for copy in system_copys:
            info_object.add_copys_system(copy)

        for (mod, proc) in copys:
            info_object.add_copys(proc, mod)

        for include in includes:
            info_object.add_sql_includes(include)

if __name__ == '__main__':
    main()

