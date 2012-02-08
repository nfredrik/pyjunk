import re
import csv
#
# Purpose of script: Get every compile errors for 
# every module. Make it possible to print out
# to a CSV file with information about:
# module name type of error, error row and file
# in subversion.
#

"""
--
compilcob.sh -f NB0130
[INFO] /srv/unireg_build/fwk/us/cobol/build/NB0130
[INFO] Start Processing NB0130 at /PROD/NBBULB
[FULLPATH] /srv/unireg_build/fwk/us/data//PROD/NBBULB/NB0130.pco
---
Precompiling NB0130.pco -> NB0130.comp5.cob

Pro*COBOL: Release 11.2.0.3.0 - Production on Thu Jan 5 09:10:52 2012

Copyright (c) 1982, 2011, Oracle and/or its affiliates.  All rights reserved.

System default option values taken from: /u01/app/oracle/product/11.2.0/client/precomp/admin/pcbcfg.cfg

---
Precompiling NB0130.comp5.cob -> NB0130.cob
---
Executing chgSQLCTXnew.sh -> NB0130.cob
SQLCTX=0
---
Compiling NB0130.cob -> NB0130.o
       INPUT-OUTPUT SECTION.                                                                                      54
*1014-E************                                                          **                                   54
**    Period missing. Period assumed.                                                                             54
---
Compiling NB0130.o -> NB0130.so
--
[OK] compiling NB0130 at /PROD/NBBULB
--
compilcob.sh -f FS3145
"""


class Module(object):
    def __init__(self, name, URL):
        self.name = name
        self.url = URL
        self.errors = []
    def __str__(self):
        return "%s" % self.name

    def set_errors(self, error):
        self.errors.append(error)

    def get_errors(self):
        return self.errors

# Read compiler log

compilerlog = open("compilation.out")

modules = []
dict = {}
sum = {}

for line in compilerlog:
    # Is this a start?
    ma = re.match("^compilcob.sh \-f\ ([A-Z0-9\-]*)", line)
    if ma != None:
        #if old name exist than save to list
        # otherwise save name temporary
        if ma.group(1) not in dict:
            dict[ma.group(1)] = 1
            latest = ma.group(1)
            mod = Module(latest,'URL')
        else:
           pass

#    mb = re.match("\*([0-9]{1-4}\-E).*([0-9]*)$", line)
    mb = re.match("^\*([0-9]*\-[ESUIW])", line)


    if mb != None:
        # We have an error if not already created, create object
        if mod not in modules:
            modules.append(mod)
        # Save error and save line
        mod.set_errors((mb.group(1)))

        if mb.group(1) not in sum:
            sum[mb.group(1)] = 1
        else:
            sum[mb.group(1)]+=1

    mc = re.match("^(PCB\-W\-[0-9]*)", line)
    if  mc != None:
        # We have an error if not already created, create object
        if mod not in modules:
            modules.append(mod)
        # Save error and save line
        mod.set_errors((mc.group(1)))

        if mc.group(1) not in sum:
            sum[mc.group(1)] = 1
        else:
            sum[mc.group(1)]+=1


#  We could a have a list of object with errors, print them to file or
#  stdout

csv_writer = csv.writer(open('errors.csv', 'wb'), delimiter = ',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(['Pro*COBOL Messages:', 'http://docs.oracle.com/cd/B10501_01/server.920/a96525/pcbeus.htm' ])
csv_writer.writerow(['MicroFocus Messages:', 'http://supportline.microfocus.com/documentation/books/sx20books/emsynt.htm' ])
#csv_writer.writerow([(key, value) for key, value in dict.iteritems()])
csv_writer.writerow([sum])


for module in modules:
    print module, module.get_errors()
    # Print name of module
    csv_writer.writerow([module]+ [err for err in module.get_errors() ])

    # Get and print errors, error row and URL to repository for module:

print sum
