#!/usr/bin/env python

import sys

#from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree.ElementTree import * 
from xml.dom import minidom




def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
#    rough_string = ElementTree.tostring(elem, 'utf-8')
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#--------------------------------------------------------------------
def set_project(top):

    top.set('name','src')
    top.set('default','cobolbuild')
    top.set('basedir','.')
    top.set('xmlns:ac','antlib:net.sf.antcontrib')
    comment = Comment('Generated for bolagsverket ab!')
    top.append(comment)

#--------------------------------------------------------------------
def set_taskdefs(top):
    child = SubElement(top, 'taskdef')
    child.set('name','cobol')
    child.set('classname','com.microfocus.ant.TaskCobol')

    child = SubElement(top, 'taskdef')
    child.set('name','cobolclean')
    child.set('classname','com.microfocus.ant.TaskCobolClean')

    child = SubElement(top, 'taskdef')
    child.set('name','cobollink')
    child.set('classname','com.microfocus.ant.TaskCobolLink')

    child = SubElement(top, 'taskdef')
    child.set('name','mffilelist')
    child.set('classname','com.microfocus.ant.TypeFileList')

    child = SubElement(top, 'taskdef')
    child.set('name','mfdirlist')
    child.set('classname','com.microfocus.ant.TypeDirectiveList')

    child = SubElement(top, 'taskdef')
    child.set('name','mfdestfilelist')
    child.set('classname','com.microfocus.ant.TypeDestinationFileList')

    child = SubElement(top, 'taskdef')
    child.set('name','mffilelist')
    child.set('classname','com.microfocus.ant.TypeFileList')

    child = SubElement(top, 'taskdef')
    child.set('uri','antlib:net.sf.antcontrib')
    child.set('resource','net/sf/antcontrib/antlib.xml')
    child.set('classpath','lib/ant-contrib-1.0b3.jar')

#--------------------------------------------------------------------
def set_os_spec_init(top):
    child = SubElement(top, 'target')
    child.set('name','os.init')

    subchild = SubElement(child, 'condition')
    subchild.set('property','windows')

    subchild = SubElement(child, 'condition')
    subchild.set('property','unix')
    
    subsubchild = SubElement(subchild, 'os')
    subsubchild.set('family','unix')
     
#--------------------------------------------------------------------
def set_cobol_compiler_directives(top):
    pass

#--------------------------------------------------------------------
def set_cobol_source_files(top):
    pass

#--------------------------------------------------------------------
def set_cobol_copybooks_locations(top):
    pass

#--------------------------------------------------------------------
def  set_cobol_source_files_and_directives(top):
    pass

#--------------------------------------------------------------------
def set_object_files(top):
    pass

#--------------------------------------------------------------------
def set_configuration_targets(top):
    pass

#--------------------------------------------------------------------
def set_general_targets(top):
    pass

#--------------------------------------------------------------------

def main(args):

    top = Element('project')

    set_project(top)

    set_taskdefs(top)

    comment = Comment('****************** OS-specific initialisation ******************')
    top.append(comment)
    set_os_spec_init(top)

    set_cobol_compiler_directives(top)

    set_cobol_source_files(top)

    set_cobol_copybooks_locations(top)

    set_cobol_source_files_and_directives(top)

    set_object_files(top)

    set_configuration_targets(top)

    set_general_targets(top)
    

#    child_with_tail = SubElement(top, 'child_with_tail')
#    child_with_tail.text = 'This child has regular text.'
#    child_with_tail.tail = 'And "tail" text.'

#    child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
#    child_with_entity_ref.text = 'This & that'

    print prettify(top)









if __name__ == '__main__':
    sys.exit(main(sys.argv))




