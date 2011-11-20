import paramiko

host = "192.168.0.23"                    #hard-coded
port = 22
transport = paramiko.Transport((host, port))

password = "hoppa2lo"                #hard-coded
username = "fredrik"                #hard-coded
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

import sys
path = './put/' + sys.argv[1]    #hard-coded
localpath = sys.argv[1]
sftp.put(localpath, path)

sftp.close()
transport.close()
print 'Upload done.'
