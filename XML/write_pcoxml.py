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
def echo_message(top, msg):
    subchild = SubElement(top, 'echo')
    subchild.set('message',msg)

#--------------------------------------------------------------------
def set_taskdefs(top):
    child = SubElement(top, 'taskdef')

    child.set('name','cobol')
    child.set('classname','com.microfocus.ant.TaskCobol')

    echo_message(top, 'cobol')

    child = SubElement(top, 'taskdef')
    child.set('name','cobolclean')
    child.set('classname','com.microfocus.ant.TaskCobolClean')

    child = SubElement(top, 'taskdef')
    child.set('name','cobollink')
    child.set('classname','com.microfocus.ant.TaskCobolLink')


    child = SubElement(top, 'taskdef')
    child.set('name','mfdestfilelist')
    child.set('classname','com.microfocus.ant.TypeDestinationFileList')

    child = SubElement(top, 'taskdef')
    child.set('uri','antlib:net.sf.antcontrib')
    child.set('resource','net/sf/antcontrib/antlib.xml')
    child.set('classpath','lib/ant-contrib-1.0b3.jar')

    child = SubElement(top, 'taskdef')
    child.set('name','mffilelist')
    child.set('classname','com.microfocus.ant.TypeFileList')

    child = SubElement(top, 'taskdef')
    child.set('name','mfdirlist')
    child.set('classname','com.microfocus.ant.TypeDirectiveList')


#--------------------------------------------------------------------
def set_os_spec_init(top):
    child = SubElement(top, 'target')
    child.set('name','os.init')

    #subchild = SubElement(child, 'condition')
    #subchild.set('property','windows')

    subchild = SubElement(child, 'condition')
    subchild.set('property','unix')
    
    subsubchild = SubElement(subchild, 'os')
    subsubchild.set('family','unix')

    child = SubElement(top, 'target')
    child.set('name','os.init.unix')
    child.set('if','os.unix')

    subchild = SubElement(child, 'property')
    subchild.set('name','ddlext')
    subchild.set('value','.so')

    subchild = SubElement(child, 'property')
    subchild.set('name','exeext')
    subchild.set('value','')

    subchild = SubElement(child, 'property')
    subchild.set('name','objext')
    subchild.set('value','.o')

    subchild = SubElement(child, 'property')
    subchild.set('name','equalsInDir')
    subchild.set('value','=')

    subchild = SubElement(child, 'property')
    subchild.set('name','pathVar')
    subchild.set('value',':')

    subchild = SubElement(child, 'property')
    subchild.set('name','shell')
    subchild.set('value','sh')

    subchild = SubElement(child, 'property')
    subchild.set('name','shell.ext')
    subchild.set('value','.sh')

    subchild = SubElement(child, 'property')
    subchild.set('name','shell.arg')
    subchild.set('value','-c')

    subchild = SubElement(child, 'property')
    subchild.set('name','script header')
    subchild.set('value','#!/bin/sh')
     
#--------------------------------------------------------------------
def set_cobol_compiler_directives(top):
    child = SubElement(top, 'mfdirlist')
    child.set('id','cobol_directive_set_1')

    subchild = SubElement(child, 'directive')
    subchild.set('name','DIALECT')
    subchild.set('value','MF')

    subchild = SubElement(child, 'directive')
    subchild.set('name','SOURCEFORMAT')
    subchild.set('value','fixed')

    subchild = SubElement(child, 'directive')
    subchild.set('name','CHARSET')
    subchild.set('value','ASCII')

    subchild = SubElement(child, 'directive')
    subchild.set('name','MAX-ERROR')
    subchild.set('value','100')

    subchild = SubElement(child, 'directive')
    subchild.set('value','COPYEXT&quot;cpy,,&quot;')

    subchild = SubElement(child, 'directive')
    subchild.set('name','SOURCETABSTOP')
    subchild.set('value','4')


    pass

#--------------------------------------------------------------------
def set_cobol_source_files(top):
    child = SubElement(top, 'mffilelist')
    child.set('id','cobol_directive_set_1')
    child.set('srcdir','${basedir}')
    child.set('type','srcfile')


    # Iterate over all cobol files
    child = SubElement(child, 'file')
    module='FUNK'
    child.set('name',module+'.pco')        ###
    relfilepath='pgm/BLB/FUNK'
    child.set('srcdir','pgm/BLB/FUNK')  ###


    pass

#--------------------------------------------------------------------
def set_cobol_copybooks_locations(top):
    child = SubElement(top, 'mffilelist')
    child.set('id','cobol.copybook.locations')

    child = SubElement(child, 'path')
    child.set('type','copybook')
    child.set('name','${src}')

    pass

#--------------------------------------------------------------------
def  set_cobol_source_files_and_directives(top):

    # Iterate

    workspace='/var/lib/jenkins/workspace/fsvTest/src/'
    filepath= workspace + 'pgm/BLB/FUNK/FUNK.pco'   ###

    child = SubElement(top, 'mfdirlist')
    #child.set('id','dirset.New_Configuration./srv/utv/devenvs/fsv/us/src37/pgm/BLB/FUNK/FUNK.pco')  ###
    child.set('id','dirset.New_Configuration.'+ filepath )  ###
    child.set('refid','cobol_directive_set_1')

    child = SubElement(top, 'mffilelist')
    child.set('refid','cobol.copybook.locations')

    child = SubElement(top, 'target')
    #child.set('name','FileCompile.New_Configuration./srv/utv/devenvs/fsv/us/src37/pgm/BLB/FUNK/FUNK.pco')  ###
    child.set('name','FileCompile.New_Configuration.'+ filepath )  ###
    child.set('depends','init')

    subchild = SubElement(child, 'cobol')
    subchild.set('desttype','obj')
    subchild.set('destdir','${basedir}/New_Configuration.bin')
    subchild.set('forceCompile','${forceCompile}')
    subchild.set('is64bit','true')
    subchild.set('threadedRts','true')

    subsubchild = SubElement(subchild, 'mffilelist')
    subsubchild.set('refid','cobol.copybook.locations')

    subsubchild = SubElement(subchild, 'mfdirlist')
    subsubchild.set('refid','dirset.New_Configuration.${filename}')

    subsubchild = SubElement(subchild, 'mffilelist')
    subsubchild.set('srcdir','${basedir}')
    subsubchild.set('type','srcfile')

    subsubsubchild = SubElement(subsubchild, 'file')
    subsubsubchild.set('name','${filename}')

    subchild = SubElement(child, 'basename')
    subchild.set('property','basename')
    subchild.set('suffix','pco')


    subchild = SubElement(child, 'cobollink')
    subchild.set('property','basename')
    subchild.set('destdir','${basedir}/New_Configuration.bin')
    subchild.set('destfile','${basename}')
    subchild.set('desttype','dll/cso')
    subchild.set('entrypoint','')
    subchild.set('is64bit','true')
    subchild.set('threadedRts','true')
    subchild.set('objectdir','${basedir}/New_Configuration.bin')
    subchild.set('objectfile','${basename}${objext}')
    pass

#--------------------------------------------------------------------
def set_object_files(top):

    child = SubElement(top, 'mffilelist')
    child.set('id','cobol.default.object.files')
    child.set('srcdir','${basedir}/${cfgtargetdir}" type="objfile')

    # Iterate
    subchild = SubElement(child, 'file')
    module='FUNK'
    #subchild.set('name','FUNK${objext}')
    subchild.set('name',module+'${objext}')

    pass

#--------------------------------------------------------------------
def set_configuration_targets(top):
    child = SubElement(top, 'target')
    child.set('name','cobol.cfg.New_Configuration')
    child.set('depends','init')

    subchild = SubElement(child, 'cobol')
    subchild.set('desttype','obj')
    subchild.set('destdir','${basedir}/New_Configuration.bin')
    subchild.set('forceCompile','${forceCompile}')
    subchild.set('is64bit','true')
    subchild.set('threadedRts','true')

    subsubchild = SubElement(subchild, 'mffilelist')
    subsubchild.set('refid','cobol.copybook.locations')

    subsubchild = SubElement(subchild, 'mfdirlist')
    subsubchild.set('refid','cobol_directive_set_1')

    subsubchild = SubElement(subchild, 'mffilelist')
    subsubchild.set('refid','cobol_file_set_1')

    # Iterate
    subchild = SubElement(child, 'cobollink')
    subchild.set('desdir','${basedir}/New_Configuration.bin')
    module='FUNK'
    subchild.set('destfile',module)  ###
    subchild.set('desttype','dll/cso')
    subchild.set('entrypoint','')
    subchild.set('threadedRts','true')
    subchild.set('is64bit','true')
    subchild.set('objectdir','${basedir}/New_Configuration.bin')
    subchild.set('objectfile',module+'${objext}') ###

    pass

#--------------------------------------------------------------------
def set_general_targets(top):


    child = SubElement(top, 'target')
    child.set('name','init.New_Configuration')
    subchild = SubElement(child, 'property')
    subchild.set('name','cfgtargetdir')
    subchild.set('value','New_Configuration.bin')


    child = SubElement(top, 'target')
    child.set('name','init')
    child.set('depends','os.init,os.init.windows,os.init.unix')
    subchild = SubElement(child, 'property')
    subchild.set('environment','env')
    subchild = SubElement(child, 'property')
    subchild.set('name','src')
    subchild.set('value','${basedir}')
    subchild = SubElement(child, 'property')
    subchild.set('name','cfg')
    subchild.set('value','New_Configuration')
    subchild = SubElement(child, 'property')
    subchild.set('name','cfgtarget')
    subchild.set('value','cfg.${cfg}')
    subchild = SubElement(child, 'property')
    subchild.set('name','forceCompile')
    subchild.set('value','true')


    child = SubElement(top, 'target')
    child.set('name','cobolbuild')
    child.set('depends','init,init.New_Configuration')
    subchild = SubElement(child, 'antcall')
    subchild.set('target','pre.build.${cfgtarget}')
    subchild.set('inheritAll','true')
    subchild = SubElement(child, 'antcall')
    subchild.set('target','cobol.${cfgtarget}')
    subchild.set('inheritAll','true')
    subchild = SubElement(child, 'antcall')
    subchild.set('target','post.build.${cfgtarget}')
    subchild.set('inheritAll','true')



    child = SubElement(top, 'target')
    child.set('name','compileNoBms')
    subchild = SubElement(child, 'antcall')
    subchild.set('target','${cfg}.FileCompile')
    subchild.set('inheritAll','true')

    child = SubElement(top, 'target')
    child.set('name','compile')
    child.set('depends','compileNoBms')

    child = SubElement(top, 'target')
    child.set('name','clean')
    child.set('depends','init,init.New_Configuration')
    subchild = SubElement(child, 'antcall')
    subchild.set('target','clean.${cfgtarget}')
    subchild.set('inheritAll','true')

#--------------------------------------------------------------------

def main(args):

    top = Element('project')

    set_project(top)

    set_taskdefs(top)

    comment = Comment('****************** OS-specific initialisation ******************')
    top.append(comment)
    set_os_spec_init(top)

    comment = Comment('****************** COBOL compiler directives ******************')
    top.append(comment)
    set_cobol_compiler_directives(top)

    comment = Comment('****************** COBOL source files ******************')
    top.append(comment)
    set_cobol_source_files(top)

    comment = Comment('****************** COBOL copybook locations ******************')
    top.append(comment)
    set_cobol_copybooks_locations(top)

    comment = Comment('****************** COBOL Source Files and Directive Set ******************')
    top.append(comment)
    set_cobol_source_files_and_directives(top)

    comment = Comment('****************** Object files ******************')
    top.append(comment)
    set_object_files(top)

    comment = Comment('****************** Configuration targets ******************')
    top.append(comment)
    set_configuration_targets(top)

    comment = Comment('****************** General targets ******************')
    top.append(comment)
    set_general_targets(top)
    

#    child_with_tail = SubElement(top, 'child_with_tail')
#    child_with_tail.text = 'This child has regular text.'
#    child_with_tail.tail = 'And "tail" text.'

#    child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
#    child_with_entity_ref.text = 'This & that'

    print prettify(top)









if __name__ == '__main__':
    sys.exit(main(sys.argv))




