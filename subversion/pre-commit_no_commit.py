#!/usr/bin/python
"""
Subversion pre-commit hook which currently checks that:

* Only the cm user

"""

import re
import sys
from commands import Commands

SVNLOOK='/usr/bin/svnlook'

def main(repos, txn, cmds=commands):

    # Check that it's the cm user that committing!
    output = commands.getoutput()
    print output

    if ('cm' != output.rstrip):
        sys.stderr.write ("Sorry, only cm allowed to commit at this stage!\n")
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s REPOS TXN\n" % (sys.argv[0]))
    else:
        cmds =Command(SVNLOOK +' author -t '+ txn + ' ' + repos)

        main(sys.argv[1], sys.argv[2], cmds=cmds)
