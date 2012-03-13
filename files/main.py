from pcoobject import PcoObject
from infoobject import InfoObject

def main():

    pco_object = PcoObject('PAOB.pco')

    # Get found copys in pco file
    copys = pco_object.get_copys()

    # Get copypaths
    proc = {}
    for module, copypath in copys:
        if copypath not in proc:
            proc[copypath] = 1

#    print proc

    # Get system copys
    system_copys = pco_object.get_copys_system()

    # Get sql includes
    includes = pco_object.get_sql_include()

    # Create a info object and copypaths
    info_object = InfoObject('PAOB.test', [k  for k in proc.iterkeys() ])    

    print "SYSTEM COPYS" * 10
    for copy in system_copys:
 #       print copy
        info_object.add_copys_system(copy)

    print "COPYS" * 10
    for (mod, proc) in copys:
#        print proc, mod
        info_object.add_copys(proc, mod)

    print "INCLUDES" * 10
    for include in includes:
#        print include
       info_object.add_sql_includes(include)

if __name__ == '__main__':
    main()

