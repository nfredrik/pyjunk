import time
import paramiko
import sys
import os
host = "lyftet_ref.filetransfer.bolagsverket.se"                    #hard-coded
port = 22

paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
transport = paramiko.Transport((host, port))

password = "wgXp79wV"      #hard-coded
username = "lyftet_ref"    #hard-coded

#path = './in/code/' + sys.argv[1]    #hard-coded
path = '.'
localpath = '/srv/home/cm/tar-archive'

def close_n_exit(conn, transp):
    conn.close()
    transp.close()
    exit(42)

def get_callback(transfered, total):
    print 'transferred bytes:', transfered, 'of total', total



def main():


    # Compare old, already fetch deliveries, and if we have any new ...
    # Works as os.listdir()
    old_dir_dict = {}
    for dir in os.listdir(localpath):
        if not os.path.isdir(dir):
            continue

        if dir not in old_dir_dict:
            old_dir_dict[dir] = 1  
    
#    print old_dir_dict
#    exit(2)

    # Log on
    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)


    sftp.chdir('.')
    sftp.getcwd()

    sftp.chdir('/in/code')
    all_dirs = sftp.listdir(path)
#    print all_dirs
 
    dir_to_fetch = []
    difference = False

    for newdir in all_dirs:
        if newdir not in old_dir_dict:
            print 'not in our dir', newdir
            difference = True
            dir_to_fetch.append(newdir)

    # There is no difference, close and exit
    if not difference:
        print 'No difference, close and exit!'
        close_n_exit(sftp, transport)
  
    # list all files in dir to fetch
    for dir in  dir_to_fetch:
        print 'dir:', dir

        files = sftp.listdir(dir)

        sftp.chdir(dir)        
        print 'changed to:', sftp.getcwd(), 'in ftp area'
        os.mkdir(dir)
        os.chdir(dir)
        print 'changed to:', os.getcwd(), 'locally'

        for file in files:
            print 'will fetch:', file,  'from:', dir
            sftp.get(file, file, get_callback)
            print sftp.stat(file)
            time.sleep(5) 
    #localpath = sys.argv[1]
    # sftp.get(localpath, path)

   
    # Start download


    print 'Download complete.'

    # Make a timestamp file for lastest run of this script

    # Mail notification to configuration management team!!



    # We ready,  close
    close_n_exit(sftp, transport)

if __name__ == '__main__':
  main()
