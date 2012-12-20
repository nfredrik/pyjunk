#!/usr/bin/env python
import sys
from xml.etree import ElementTree

with open('pcobolBuild', 'rt') as f:
    tree = ElementTree.parse(f)

print tree

#for node in tree.iter():   2.7 and later
for node in tree.getiterator():
    print node.tag, node.attrib
sys.exit(0)


for node in tree.getiterator('file'):
    name = node.attrib.get('name')
    if name:
        print ' %s' %  name

for node in tree.getiterator('file'):
    name = node.attrib.get('name')
    if name:
        print ' %s' %  name
