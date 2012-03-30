#!/usr/bin/python
"""
Subversion pre-commit hook which currently checks that:

* Only cm can commit at this stage

* Make it impossible to commit to a tag, since it should be regarded as read-only

* The commit contains a commit message to avoid commiting empty changesets which 
  tortoisesvn seems to have a habbit of committing.
"""

import os
import re
import sys
import commands

LEN_OF_COMMIT_MSG = 5
SVNLOOK='/usr/bin/svnlook'
cmguys =  ['cm', 'jje', 'olk', 'fsv']

def main(repos, txn):

    log_msg = commands.getoutput(SVNLOOK +' changed -t '+ txn + ' ' + repos)

    # Check that it's a cm guy that's committing!
    author = commands.getoutput(SVNLOOK + ' author ' + repos)

    if  author.rstrip() not in cmguys and re.match('^.*trunk\/.*$', log_msg.rstrip()) != None:
        sys.stderr.write ("Sorry, only cm guys allowed to commit to trunk at this phase of the project!\n")
        sys.exit(1)

    # Check if attempt to commit in tag
    if (re.match('^U\W.*tags\/.*$', log_msg.rstrip()) != None):
        sys.stderr.write ("Sorry, tags read-only, not allowed to commit!\n")
        sys.exit(1)

    # Check if valid commit message  

    if len(log_msg) < LEN_OF_COMMIT_MSG:
        sys.stderr.write ("Please enter a commit message which details what has changed during this commit.\n")
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s REPOS TXN\n" % (sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])


