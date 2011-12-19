#!/usr/bin/python
"""
Subversion postcommit hook which currently checks that:

* Send email to team leaders when someone tags...

"""

import re
import sys
import commands
from Mail import Mail

SVNLOOK='/usr/bin/svnlook'

def main(repopath, rev):

    # Check if attempt to commit in tag
    log_msg = commands.getoutput(SVNLOOK +' changed -r '+ rev + ' ' + repopath)
    if (re.match('^U\W.*tags\/.*$', log_msg.rstrip()) != None):
        # send mail to team leaders?
        mail = Mail(to = 'fredrik.svard@bolagsverket.se',
                    username =  'The configuration team',
                    password = 'halli hallo',
                    server =  'ad01.bolagsverket.se',
                    )

        mail.send('Created new tag:' + repopath + ' revision' + rev)

    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s REPOS-PATH REV\n" % (sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])
