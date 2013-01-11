#!/usr/bin/env python

import sys
import os

from xml.etree.ElementTree import * 
from xml.dom import minidom


#--------------------------------------------------------------------
def echo_message(top, msg):
    subchild = SubElement(top, 'echo')
    subchild.set('message',msg)

#--------------------------------------------------------------------

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
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

    echo_message(top, 'cobol')

    child = SubElement(top, 'taskdef')
    child.set('name','cobolclean')
    child.set('classname','com.microfocus.ant.TaskCobolClean')

    child = SubElement(top, 'taskdef')
    child.set('name','cobollink')
    child.set('classname','com.microfocus.ant.TaskCobolLink')

    child = SubElement(top, 'taskdef')
    child.set('uri','antlib:net.sf.antcontrib')
    child.set('resource','net/sf/antcontrib/antlib.xml')
    child.set('classpath','lib/ant-contrib-1.0b3.jar')

    child = SubElement(top, 'typedef')
    child.set('name','mfdestfilelist')
    child.set('classname','com.microfocus.ant.TypeDestinationFileList')

    child = SubElement(top, 'typedef')
    child.set('name','mffilelist')
    child.set('classname','com.microfocus.ant.TypeFileList')

    child = SubElement(top, 'typedef')
    child.set('name','mfdirlist')
    child.set('classname','com.microfocus.ant.TypeDirectiveList')


#--------------------------------------------------------------------
def set_os_spec_init(top):
    child = SubElement(top, 'target')
    child.set('name','os.init')

    subchild = SubElement(child, 'condition')
    subchild.set('property','unix')
    
    subsubchild = SubElement(subchild, 'os')
    subsubchild.set('family','unix')

    child = SubElement(top, 'target')
    child.set('name','os.init.unix')
    child.set('if','unix')

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

    subchild = SubElement(child, 'directives')
    subchild.set('value','COPYEXT"cpy,,"')

    subchild = SubElement(child, 'directive')
    subchild.set('name','SOURCETABSTOP')
    subchild.set('value','4')

#--------------------------------------------------------------------
def set_cobol_source_files_header(top):
    child = SubElement(top, 'mffilelist')
    child.set('id','cobol_file_set_1')
    child.set('srcdir','${basedir}')
    child.set('type','srcfile')
    return child
 
   ###
def set_cobol_source_files(child,module='FUNK',relpath='pgm/BLB/FUNK'):
    """ Iterate over all cobol files"""
    child = SubElement(child, 'file')
    child.set('name',module+'.pco')     
    child.set('srcdir',relpath)

#--------------------------------------------------------------------
def set_cobol_copybooks_locations(top):
    child = SubElement(top, 'mffilelist')
    child.set('id','cobol.copybook.locations')

    child = SubElement(child, 'path')
    child.set('type','copybook')
    child.set('name','${src}')

#--------------------------------------------------------------------
def  set_cobol_source_files_and_directives(top, module='FUNK',workspace='/var/lib/jenkins/workspace/fsvTest/src',relpath='pgm/BLB/FUNK' ):

    """Iterate for all cobol modules"""

    #filepath= workspace + relpath + module +'.pco'
    filepath= workspace +  relpath + '/' + module +'.pco'

    child = SubElement(top, 'mfdirlist')
    child.set('id','dirset.New_Configuration.'+ filepath )  ###
    child.set('refid','cobol_directive_set_1')

    child = SubElement(top, 'mffilelist')
    child.set('refid','cobol.copybook.locations')

    child = SubElement(top, 'target')
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
    subchild.set('file','${filename}')
    subchild.set('suffix','pco')


    subchild = SubElement(child, 'cobollink')
    subchild.set('destdir','${basedir}/New_Configuration.bin')
    subchild.set('destfile','${basename}')
    subchild.set('desttype','dll/cso')
    subchild.set('entrypoint','')
    subchild.set('threadedRts','true')
    subchild.set('is64bit','true')
    subchild.set('objectdir','${basedir}/New_Configuration.bin')
    subchild.set('debug','true')
    subchild.set('objectfile','${basename}${objext}')

#--------------------------------------------------------------------
def set_object_files_header(top):
    child = SubElement(top, 'mffilelist')
    child.set('id','cobol.default.object.files')
    child.set('srcdir','${basedir}/${cfgtargetdir}')
    child.set('type','objfile')
    return child

#--------------------------------------------------------------------
def set_object_files(child, module='FUNK'):

    subchild = SubElement(child, 'file')
    subchild.set('name',module+'${objext}')

#--------------------------------------------------------------------
def set_configuration_targets_header(top):
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
    return child

def set_configuration_targets(child, module='FUNK' ):

    # Iterate
    subchild = SubElement(child, 'cobollink')
    subchild.set('destdir','${basedir}/New_Configuration.bin')
    subchild.set('destfile',module)  ###
    subchild.set('desttype','dll/cso')
    subchild.set('entrypoint','')
    subchild.set('threadedRts','true')
    subchild.set('is64bit','true')
    subchild.set('objectdir','${basedir}/New_Configuration.bin')
    subchild.set('objectfile',module+'${objext}') ###


def set_configuration_targets_end(top):

    child = SubElement(top, 'target')
    child.set('name','New_Configuration.FileCompile')
    child.set('depends','init')
    subchild = SubElement(child, 'ac:for')
    subchild.set('list','${filesList}')
    subchild.set('param','filename')
    subchild.set('keepgoing','true')
    subchild.set('trim','true')
    subchild2 = SubElement(subchild, 'sequential')
    subchild3 = SubElement(subchild2, 'ac:if')
    subchild4 = SubElement(subchild3, 'not')
    subchild5 = SubElement(subchild4, 'isset')
    subchild5.set('property','isCancelled')
    subchild6 = SubElement(subchild3, 'then')
    subchild7 = SubElement(subchild6, 'ac:antcallback')
    subchild7.set('target','FileCompile.New_Configuration.@{filename}')
    subchild7.set('inheritAll','true')
    subchild7.set('return','isCancelled')
    subchild8 = SubElement(subchild7, 'param')
    subchild8.set('name','filename')
    subchild8.set('value','@{filename}')

    child = SubElement(top, 'target')
    child.set('name','clean.cfg.New_Configuration')
    child.set('depends','init')
    child1 = SubElement(child, 'cobolclean')
    child1.set('desttype','dll')
    child1.set('destdir','${basedir}/New_Configuration.bin')
    child1.set('debug','true')
    child2 = SubElement(child1, 'mffilelist')
    child2.set('refid','cobol_file_set_1')

    child = SubElement(top, 'target')
    child.set('name','pre.build.cfg.New_Configuration')
    child.set('depends','init')

    child = SubElement(top, 'target')
    child.set('name','post.build.cfg.New_Configuration')
    child.set('depends','init')

#--------------------------------------------------------------------
def set_general_targets(top):

    child = SubElement(top, 'target')
    child.set('name','init.New_Configuration')
    subchild = SubElement(child, 'property')
    subchild.set('name','cfgtargetdir')
    subchild.set('value','New_Configuration.bin')


    child = SubElement(top, 'target')
    child.set('name','init')
    child.set('depends','os.init, os.init.unix')
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
def create_cobol_dict(workSpace):
    cobol_files ={}
    for root, dirs, files in os.walk(workSpace):
        for file in files:
            if file.endswith('.pco'):
                #print file
                relpath = root.replace(workSpace,'')
                #print relpath
                cobol_files[file.replace('.pco','')]= root.replace(workSpace,'')

    return cobol_files

def main(args):

    #JenkinsWorkspace = args[1]
    #workSpace= JenkinsWorkspace + '/src/'
    workSpace='/var/lib/jenkins/workspace/fsvTest/src'

    #buildFile = args[2]

    cobol_dict = create_cobol_dict(workSpace)
    #print cobol_dict

    #for key, value in cobol_dict.items():
    #    print key, value

    #return 1

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
    child = set_cobol_source_files_header(top)
    # Iterate
    #set_cobol_source_files(child)
    #set_cobol_source_files(child,module='BEHOR',relpath='pgm/BLB/INLFIL1')
    
    for module, path in cobol_dict.items():
        set_cobol_source_files(child,module=module,relpath=path)

    comment = Comment('****************** COBOL copybook locations ******************')
    top.append(comment)
    set_cobol_copybooks_locations(top)

    comment = Comment('****************** COBOL Source Files and Directive Set ******************')
    top.append(comment)
    # Iterate
    #set_cobol_source_files_and_directives(top)
    # set_cobol_source_files_and_directives(top,module='BEHOR',workspace=workSpace,relpath= 'pgm/BLB/INLFIL1/')

    for module, path in cobol_dict.items():
        set_cobol_source_files_and_directives(top,module=module,workspace=workSpace,relpath= path)

    comment = Comment('****************** Object files ******************')
    top.append(comment)

    child = set_object_files_header(top)
    #set_object_files(child)
    #set_object_files(child, module='BEHOR')

    for module, path in cobol_dict.items():
        set_object_files(child, module=module)

    comment = Comment('****************** Configuration targets ******************')
    top.append(comment)
    child = set_configuration_targets_header(top)
    # Iterate
    #set_configuration_targets(child)
    #set_configuration_targets(child, module='BEHOR')

    for module, path in cobol_dict.items():
        set_configuration_targets(child, module=module)

    set_configuration_targets_end(top)

    comment = Comment('****************** General targets ******************')
    top.append(comment)
    set_general_targets(top)

    print prettify(top)

    # Save everything to file
    #with open(buildFile,'wb') as fw:
    #    fw.write(prettify(top))

if __name__ == '__main__':
    sys.exit(main(sys.argv))




