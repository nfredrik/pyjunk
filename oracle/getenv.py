import os

print 'COBCONFIG, Tailor runtime  configurable options:',os.getenv('COBCONFIG')
print 'COBCPY, Locates copyfiles :', os.getenv('COBCPY')
print 'COBDATA, Locates datafiles :', os.getenv('COBDATA')
print 'COBDIR, Locates COBOL system software:', os.getenv('COBDIR')
print 'COBIDY, Locates COBOL Animator informations files:', os.getenv('COBIDY')
print 'COBOPT, Specifies user default Cob utility options:', os.getenv('COBOPT')
print 'COBPATH, Locates programs for dynamic loading:'
for p in  os.getenv('COBPATH').split(':'):
    print p

print 'LD_LIBRARY_PATH, Locates shared libraries:'
for p in os.getenv('LD_LIBRARY_PATH').split(':'):
    print p

