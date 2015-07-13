
import os

all_cfiles = [file for file in os.listdir('.') if file.endswith('.c')]

for file in all_cfiles:
    with open(file, 'r') as fh:
        tot = fh.readlines()
        #print(tot)
        for row in tot:
            if "AG6" in row:
                print(row) 