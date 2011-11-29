#!/usr/bin/python
"""
Subversion pre-commit hook which currently checks that:

* Make it impossible to commit to a tag, that for some reason always be read-only

* The commit contains a commit message to avoid commiting empty changesets which 
  tortoisesvn seems to have a habbit of committing.

Based on http://svn.collab.net/repos/svn/branches/1.2.x/contrib/hook-scripts/commit-block-joke.py
and hooks/pre-commit.tmpl

Hacked together by Jacques Marneweck <jacques@php.net>
"""

import re
import sys
import commands

SVNLOOK='/usr/bin/svnlook'

def main(repos, txn):

    # Check if attempt to commit in tag
    log_msg = commands.getoutput(SVNLOOK +' changed -t '+ txn + ' ' + repos)
    if (re.match('^U\W.*tags\/.*$', log_msg.rstrip()) != None):
        sys.stderr.write ("Sorry, tags read-only, not allowed to commit!\n")
        sys.exit(1)

    # Check if valid commit message  
    log_msg = commands.getoutput(SVNLOOK +' log -t '+ txn + ' ' + repos).rstrip()

    if len(log_msg) < 10:
        sys.stderr.write ("Please enter a commit message which details what has changed during this commit.\n")
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s REPOS TXN\n" % (sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])
