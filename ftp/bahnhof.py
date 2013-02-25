
from ftplib import FTP

ftp = FTP('privat.bahnhof.se') 

ftp.login(user='wb177225', passwd='94e6a11d6')

# FTP.storbinary(command, file[, blocksize, callback, rest])
ftp.storbinary('STOR index.html', open('index.html', 'rb'))

ftp.quit()

