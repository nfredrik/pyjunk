#!/usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree.ElementTree import * 
from xml.dom import minidom




def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
#    rough_string = ElementTree.tostring(elem, 'utf-8')
    #rough_string = tostring(elem, 'utf-8')
    #rough_string = tostring(elem, 'ISO-8859-15')
    rough_string = tostring(elem)
    # 
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")



def main(args):
    pass

    top = Element('top')

    comment = Comment('Generated for PyMOTW')
    top.append(comment)

    child = SubElement(top, 'child')
    child.text = 'This child contains text.'

    child_with_tail = SubElement(top, 'child_with_tail')
    child_with_tail.text = 'This child has regular text.'
    child_with_tail.tail = 'And "tail" text.'

    child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
    child_with_entity_ref.text = 'This & that'
 
    for i in range(2):
        child = SubElement(top, 'filelist')
        child.set('name','olle')
  

    print prettify(top)









if __name__ == '__main__':
    sys.exit(main(sys.argv))




