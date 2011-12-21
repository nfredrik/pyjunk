from command import Command
import os

def main():

    hash = {}
   
    ls_obj = Command('find .')

    for l in ls_obj.get_list_output():
        if os.path.basename(l) not in hash:
            hash[os.path.basename(l)] = l
        else:
            if not os.path.isdir(hash[os.path.basename(l)]) and not os.path.isdir(l):
                print 'duplicate:'
                print '1st:', hash[os.path.basename(l)]
                print '2nd:', l
                cmd = 'cmp ' + hash[os.path.basename(l)] + ' ' + l
#                print 'execute:' , cmd 
                cmp_obj = Command(cmd)
                if cmp_obj.get_status():
                    print 'different'
                else:
                    print 'identical'

if __name__ == "__main__":
  main()
