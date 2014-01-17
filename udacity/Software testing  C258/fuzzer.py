#!usr/bin/python
############ constants

apps = ["/Applications/Adobe Reader.app/Contents/MacOS/AdobeReader",
     "/Applications/Preview.app/Contents/MacOS/Preview"
     ]

file_list = ["sample1.pdf"]

fuzz_output = "fuzzed.pdf"

FuzzFactor = 250
num_tests = 10000
############# code

import math
import random
import string
import subprocess
import time

for i in range(num_tests):
  file_choice = random.choice(file_list)
  app = random.choice(apps)

  buf = bytearray(open(file_choice, 'rb').read())

  numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1

  for j in range(numwrites):
    rbyte = random.randrange(256)
    rn = random.randrange(len(buf))
    buf[rn] = "%c" % (rbyte)

  open(fuzz_output, 'wb').write(buf)

  print 'call with:'
  print 'app', app
  print 'fuzz_output', fuzz_output
  
  process = subprocess.Popen([app, fuzz_output])

  time.sleep(4)
  crashed = process.poll()

  if not crashed:
    process.terminate()