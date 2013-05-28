#!/usr/bin/env python
import sys
from xml.etree import ElementTree

with open('config.xml', 'rt') as f:
    tree = ElementTree.parse(f)

#
fn = tree.find("blockingJobs/cdbisboCDBI")

print fn

sys.exit(0)

#for node in tree.iter():   2.7 and later

#  tag: blockingJobs
for node in tree.getiterator():
#    print node.tag, '::', node.attrib
    print node.tag, '::', node.text
sys.exit(0)


for node in tree.getiterator('file'):
    name = node.attrib.get('name')
    if name:
        print ' %s' %  name

for node in tree.getiterator('file'):
    name = node.attrib.get('name')
    if name:
        print ' %s' %  name
