from command import Command
from filestatus import FileStatus
import os

def main():

    hash = {}
   
    files = Command('find .')

    for file in files.get_list_output():
        file_status = FileStatus(file)
        if file_status.invalid_file():
            print file, ' invalid'

        if file_status.executable():
            pass
#            print file, 'executable...'

if __name__ == "__main__":
  main()
