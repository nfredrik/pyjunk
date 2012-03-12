from pcoobject import PcoObject
from infoobject import InfoObject

def main():

    pco_object = PcoObject('PAOB.pco')


    copys = pco_object.get_copys()

    proc = {}
    for m, p in copys:
        if p not in proc:
            proc[p] = 1

#    print proc

    system_copys = pco_object.get_copys_system()

    includes = pco_object.get_sql_include()

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

