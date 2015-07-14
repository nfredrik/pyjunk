
import os

all_cfiles = [file for file in os.listdir('.') if file.endswith('.c')]

used = list()

for file in all_cfiles:
    with open(file, 'r') as fh:
        tot = fh.readlines()
        for i, row in enumerate(tot):
            if "AG6" in row:
                print(row.strip(), end=' ')
                if '"' in tot[i+1]: 
                    print(tot[i+1].strip())