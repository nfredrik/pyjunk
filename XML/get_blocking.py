#!/usr/bin/env python
import sys
from xml.etree import ElementTree

OK, ERROR = 0,1

#JENKINS_HOME_JOBS_SPACE = '/var/lib/jenkins/jobs/'
JENKINS_HOME_JOBS_SPACE = './'
JENKINS_CONFIG_FILE = '/config.xml'


def main(args):

    if len(args) != 2:
        print 'Error: We need name of job and name of CDBI-job as argument'
        return ERROR

    print 'jobname:', args[0]
    jobname = args[0]
    print 'CDBIjobname:', args[1]
    cdbi_jobname = args[1]

    PATH =  JENKINS_HOME_JOBS_SPACE + jobname + JENKINS_CONFIG_FILE

    tree = ElementTree.parse(PATH)

    for node in tree.getiterator():
        if node.tag == "blockingJobs":
            print node.tag, '::', node.text
            node.text = cdbi_jobname
            tree.write(PATH)
            return OK

    return ERROR

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or [0]))



