#!/usr/bin/python
"""
Subversion pre-commit hook which currently checks that:
* That only the cm can commit
"""
OK, ERROR = 0,1

import os
import re
import sys
from command import Command

SVNLOOK='/usr/bin/svnlook'

def main(repos, txn, cmds):

    # Check that it's the cm user that committing!
    output = cmds.get_string_output()

    print repos, txn, output

    print 'basename' , os.path.basename(repos)

    if 'trunk' == os.path.basename(repos) and 'cm' != output.rstrip():
        sys.stderr.write ("Sorry, only cm allowed to commit to trunk at this phase of the project!\n")
        return ERROR

    return OK

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s REPOS TXN\n" % (sys.argv[0]))
    else:
        cmds =Command(SVNLOOK +' author -t '+ txn + ' ' + repos)

        sys.exit(main(sys.argv[1], sys.argv[2], cmds=cmds))
