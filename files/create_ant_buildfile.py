#!/usr/bin/env python
"""
Copyright Bolagsverket AB

Script that generates a buildfile based on source code files residing in the repository and specifically
in this checkout.

The script takes workspace as argument and assumes that all source code files resides under pgm.

"""
import sys
import os
import re
import pickle
from xml.etree.ElementTree import * 
from xml.dom import minidom
    
class PcoObject(object):
    """
    A object to hold some attributes about a pco file
    """
    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath
        self.filehandle = open(filename,'r')
        self.read_from_file(self.filehandle)
        self.copys = dict()

    def read_from_file(self, fh):
         self.string = fh.read()
         self.filehandle.close()

    def get_filename(self):
        return  os.path.basename(os.path.splitext(self.filename)[0])

    def get_program_id(self):
        """
        Return the filename as a string
        """
        self.name = re.search('PROGRAM\-ID\.[\s]*(\'[\w]*\')', self.string)
        if self.name != None:
            return self.name.group(1)

        self.name = re.search('PROGRAM\-ID\.[\s]*([\w]*)', self.string)
        if self.name != None:
            return self.name.group(1)

    def get_filepath(self):
        return self.filepath

    def get_sql_include(self):
        """
        Return found SQL INCLUDES in a list
        """
        """HPCLLA     EXEC SQL INCLUDE 'BOTSSS030FTD' END-EXEC."""
        self.sqls = re.findall(r"^[\w\d\_\-\ ]{6}[^\*][\s]*EXEC[\s]*SQL[\s]*INCLUDE[\s]*\'([\w\d\-\_]*)\'", self.string, re.MULTILINE)
        return self.sqls
    
    def set_copys(self, copydict):
        """
        Pass a dictionary of copybooks, key=modulename, value=path
        """
        for copy in self.get_sql_include():
            if  copy+'.cpy' in copydict:
                self.copys[ copy+'.cpy'] = copydict[ copy+'.cpy']
                
    def get_copys(self):
        return self.copys

#--------------------------------------------------------------------

class PcoBuilder(object):
    """
    Build a list of pco objects and set some attributes
    """

    def __init__(self, workSpace):
        
        self.workspace = workSpace
        """
        Find all pco files and make a list of them
        """
        self.pco_files = list()

        for dirpath, dirnames, filenames in os.walk(self.workspace):
            for filename in filenames:
                if filename.endswith('pco'):
                    self.pco_files.append(PcoObject(dirpath + '/' + filename, dirpath.replace(workSpace, '')))                
                
                
        """ Find all copys """
        self.get_all_copys()
    
        """ Update all pco with path to the copys """
        for pco in self.pco_files:
            pco.set_copys(self.all_copys)
    def get_all_copys(self):
        self.all_copys = dict()
    
        for root, dirs, files in os.walk(self.workspace):
             for file in files:
                  if file.endswith('.cpy'):
                       if file not in self.all_copys:
                           self.all_copys[file] = root.replace(self.workspace, '')
                       else:
                           print 'Error: duplicate of file!'
                           print 'File:', file
                           print 'current:', self.all_copys[file]
                           print 'new:', root    
#--------------------------------------------------------------------
def echo_message(top, msg):
    """
    In case we need to echo something
    """
    subchild = SubElement(top, 'echo')
    subchild.set('message', msg)
#--------------------------------------------------------------------
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#--------------------------------------------------------------------

def write_dict_2_file(dic, afile):
    """ Save dictionary as a pickle file
    """
    output = open(afile, 'wb')
    pickle.dump(dic, output)
    output.close() 
    
#--------------------------------------------------------------------

class BuildFile(object):
    def __init__(self, buildfile):
        self.top = Element('project')
        self.buildfile = buildfile
       
        self.source_header = None
        self.obj_header = None 
        self.targets_header = None      
    def set_project(self):
        """
        Okey, this is the top of the build file ...
        """
        self.top.set('name', 'src')
        self.top.set('default', 'cobolbuild')
        self.top.set('basedir', '.')
        self.top.set('xmlns:ac', 'antlib:net.sf.antcontrib')
        comment = Comment('Generated at Bolagsverket ab!')
        self.top.append(comment)
    def set_taskdefs(self):
        """
        Include stuff from MicroFocus to be able to invoke compiler,  linker and so on...
        """
        child = SubElement(self.top, 'taskdef')

        child.set('name', 'cobol')
        child.set('classname', 'com.microfocus.ant.TaskCobol')

        echo_message(self.top, 'Bolagsverkets dynamic buildfile')

        child = SubElement(self.top, 'taskdef')
        child.set('name', 'cobolclean')
        child.set('classname', 'com.microfocus.ant.TaskCobolClean')

        child = SubElement(self.top, 'taskdef')
        child.set('name', 'cobollink')
        child.set('classname', 'com.microfocus.ant.TaskCobolLink')

        child = SubElement(self.top, 'taskdef')
        child.set('uri', 'antlib:net.sf.antcontrib')
        child.set('resource', 'net/sf/antcontrib/antlib.xml')
        child.set('classpath', 'lib/ant-contrib-1.0b3.jar')

        child = SubElement(self.top, 'typedef')
        child.set('name', 'mfdestfilelist')
        child.set('classname', 'com.microfocus.ant.TypeDestinationFileList')

        child = SubElement(self.top, 'typedef')
        child.set('name', 'mffilelist')
        child.set('classname', 'com.microfocus.ant.TypeFileList')

        child = SubElement(self.top, 'typedef')
        child.set('name', 'mfdirlist')
        child.set('classname', 'com.microfocus.ant.TypeDirectiveList')

        child = SubElement(self.top, 'taskdef')
        child.set('resource', 'net/sf/antcontrib/antcontrib.properties')                   
    def set_os_spec_init(self):
        """
        Okey we running linux/unix here
        """
        
        comment = Comment('****************** OS-specific initialisation ******************')
        self.top.append(comment)
        child = SubElement(self.top, 'target')
        child.set('name', 'os.init')

        subchild = SubElement(child, 'condition')
        subchild.set('property', 'unix')
    
        subsubchild = SubElement(subchild, 'os')
        subsubchild.set('family', 'unix')

        child = SubElement(self.top, 'target')
        child.set('name', 'os.init.unix')
        child.set('if', 'unix')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'ddlext')
        subchild.set('value', '.so')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'exeext')
        subchild.set('value', '')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'objext')
        subchild.set('value', '.o')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'equalsInDir')
        subchild.set('value', '=')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'pathVar')
        subchild.set('value', ':')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'shell')
        subchild.set('value', 'sh')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'shell.ext')
        subchild.set('value', '.sh')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'shell.arg')
        subchild.set('value', '-c')

        subchild = SubElement(child, 'property')
        subchild.set('name', 'script header')
        subchild.set('value', '#!/bin/sh')
    def set_cobol_compiler_directives(self):
        """
        Add som ordinary compiler directives
        """
        child = SubElement(self.top, 'mfdirlist')
        child.set('id', 'cobol_directive_set_1')

        subchild = SubElement(child, 'directive')
        subchild.set('name', 'DIALECT')
        subchild.set('value', 'MF')

        subchild = SubElement(child, 'directive')
        subchild.set('name', 'SOURCEFORMAT')
        subchild.set('value', 'fixed')

        subchild = SubElement(child, 'directive')
        subchild.set('name', 'CHARSET')
        subchild.set('value', 'ASCII')

        subchild = SubElement(child, 'directive')
        subchild.set('name', 'MAX-ERROR')
        subchild.set('value', '100')

        subchild = SubElement(child, 'directives')
        subchild.set('value', 'COPYEXT"cpy,,"')

        subchild = SubElement(child, 'directive')
        subchild.set('name', 'SOURCETABSTOP')
        subchild.set('value', '4')      
    def set_cobol_source_files_header(self):
        """
        Start prepare for the source code files that will be added
        """
        comment = Comment('****************** COBOL source files ******************')
        self.top.append(comment)
        self.source_header = SubElement(self.top, 'mffilelist')
        self.source_header.set('id', 'cobol_file_set_1')
        self.source_header.set('srcdir', '${basedir}')
        self.source_header.set('type', 'srcfile')        
    def set_cobol_source_files(self, module, relpath):
        """
        Source code files ...
        """
        child = SubElement(self.source_header, 'file')
        child.set('name', module +'.pco')     
        child.set('srcdir', relpath)
    def set_cobol_copybooks_locations(self):
        """
        Some general stuff about the copybooks
        """
        
        comment = Comment('****************** COBOL copybook locations ******************')
        self.top.append(comment)        
        child = SubElement(self.top, 'mffilelist')
        child.set('id', 'cobol.copybook.locations')

        child = SubElement(child, 'path')
        child.set('type', 'copybook')
        child.set('name', '${src}')
    def set_cobol_source_files_and_directives(self , module, workspace, relpath ):
        """
        This core stuff. Called when we ready to compile
        """

        comment = Comment('****************** COBOL Source Files and Directive Set ******************')
        self.top.append(comment)
        
        filepath = workspace +  relpath + '/' + module +'.pco'
            
        child = SubElement(self.top, 'mfdirlist')
        child.set('id', 'dirset.New_Configuration.'+ filepath )
        child.set('refid', 'cobol_directive_set_1')
    
        child = SubElement(self.top, 'mffilelist')
        child.set('refid', 'cobol.copybook.locations')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'FileCompile.New_Configuration.'+ filepath )
        child.set('depends', 'init')
    
        subchild = SubElement(child, 'cobol')
        subchild.set('desttype', 'obj')
        subchild.set('destdir', '${basedir}/New_Configuration.bin')
        subchild.set('forceCompile', '${forceCompile}')
        subchild.set('is64bit', 'true')
        subchild.set('threadedRts', 'true')
    
        subsubchild = SubElement(subchild, 'mffilelist')
        subsubchild.set('refid', 'cobol.copybook.locations')
    
        subsubchild = SubElement(subchild, 'mfdirlist')
        subsubchild.set('refid', 'dirset.New_Configuration.${filename}')
    
        subsubchild = SubElement(subchild, 'mffilelist')
        subsubchild.set('srcdir', '${basedir}')
        subsubchild.set('type', 'srcfile')
    
        subsubsubchild = SubElement(subsubchild, 'file')
        subsubsubchild.set('name', '${filename}')
    
        subchild = SubElement(child, 'basename')
        subchild.set('property', 'basename')
        subchild.set('file', '${filename}')
        subchild.set('suffix', 'pco')
    
        subchild = SubElement(child, 'cobollink')
        subchild.set('destdir', '${basedir}/New_Configuration.bin')
        subchild.set('destfile', '${basename}')
        subchild.set('desttype', 'dll/cso')
        subchild.set('entrypoint', '')
        subchild.set('threadedRts', 'true')
        subchild.set('is64bit', 'true')
        subchild.set('objectdir', '${basedir}/New_Configuration.bin')
        subchild.set('debug', 'true')
        subchild.set('objectfile', '${basename}${objext}')       
    def set_object_files_header(self):
        """
        Something about object files
        """

        comment = Comment('****************** Object files ******************')
        self.top.append(comment)

        self.obj_header = SubElement(self.top, 'mffilelist')
        self.obj_header.set('id', 'cobol.default.object.files')
        self.obj_header.set('srcdir', '${basedir}/${cfgtargetdir}')
        self.obj_header.set('type', 'objfile')
    def set_object_files(self, module):

        child = SubElement(self.obj_header, 'file')
        child.set('name', module + '${objext}')     
    def set_configuration_targets_header(self):
        """
        """
        child = SubElement(self.top, 'target')
        child.set('name', 'cobol.cfg.New_Configuration')
        child.set('depends', 'init')
    
        subchild = SubElement(child, 'cobol')
        subchild.set('desttype', 'obj')
        subchild.set('destdir', '${basedir}/New_Configuration.bin')
        subchild.set('forceCompile', '${forceCompile}')
        subchild.set('is64bit', 'true')
        subchild.set('threadedRts', 'true')
    
        subsubchild = SubElement(subchild, 'mffilelist')
        subsubchild.set('refid', 'cobol.copybook.locations')
    
        subsubchild = SubElement(subchild, 'mfdirlist')
        subsubchild.set('refid', 'cobol_directive_set_1')
    
        subsubchild = SubElement(subchild, 'mffilelist')
        subsubchild.set('refid', 'cobol_file_set_1')
        self.targets_header = child 
    def set_configuration_targets(self, module):
        """
        """
        subchild = SubElement(self.targets_header, 'cobollink')
        subchild.set('destdir', '${basedir}/New_Configuration.bin')
        subchild.set('destfile', module)
        subchild.set('desttype', 'dll/cso')
        subchild.set('entrypoint', '')
        subchild.set('threadedRts', 'true')
        subchild.set('is64bit', 'true')
        subchild.set('objectdir', '${basedir}/New_Configuration.bin')
        subchild.set('objectfile', module + '${objext}')
    def set_configuration_targets_end(self):
        """
        """
        
        comment = Comment('****************** Configuration targets ******************')
        self.top.append(comment)
        child = SubElement(self.top, 'target')
        child.set('name', 'New_Configuration.FileCompile')
        child.set('depends', 'init')
        subchild = SubElement(child, 'ac:for')
        subchild.set('list', '${filesList}')
        subchild.set('param', 'filename')
        subchild.set('keepgoing', 'true')
        subchild.set('trim', 'true')
        subchild2 = SubElement(subchild, 'sequential')
        subchild3 = SubElement(subchild2, 'ac:if')
        subchild4 = SubElement(subchild3, 'not')
        subchild5 = SubElement(subchild4, 'isset')
        subchild5.set('property', 'isCancelled')
        subchild6 = SubElement(subchild3, 'then')
        subchild7 = SubElement(subchild6, 'ac:antcallback')
        subchild7.set('target', 'FileCompile.New_Configuration.@{filename}')
        subchild7.set('inheritAll', 'true')
        subchild7.set('return', 'isCancelled')
        subchild8 = SubElement(subchild7, 'param')
        subchild8.set('name', 'filename')
        subchild8.set('value', '@{filename}')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'clean.cfg.New_Configuration')
        child.set('depends', 'init')
        child1 = SubElement(child, 'cobolclean')
        child1.set('desttype', 'dll')
        child1.set('destdir', '${basedir}/New_Configuration.bin')
        child1.set('debug', 'true')
        child2 = SubElement(child1, 'mffilelist')
        child2.set('refid', 'cobol_file_set_1')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'pre.build.cfg.New_Configuration')
        child.set('depends', 'init')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'post.build.cfg.New_Configuration')
        child.set('depends', 'init')              
    def set_general_targets(self):
        """
        """
        comment = Comment('****************** General targets ******************')
        self.top.append(comment)
        
        child = SubElement(self.top, 'target')
        child.set('name', 'init.New_Configuration')
        subchild = SubElement(child, 'property')
        subchild.set('name', 'cfgtargetdir')
        subchild.set('value', 'New_Configuration.bin')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'init')
        child.set('depends', 'os.init, os.init.unix')
        subchild = SubElement(child, 'property')
        subchild.set('environment', 'env')
        subchild = SubElement(child, 'property')
        subchild.set('name', 'src')
        subchild.set('value', '${basedir}')
        subchild = SubElement(child, 'property')
        subchild.set('name', 'cfg')
        subchild.set('value', 'New_Configuration')
        subchild = SubElement(child, 'property')
        subchild.set('name', 'cfgtarget')
        subchild.set('value', 'cfg.${cfg}')
        subchild = SubElement(child, 'property')
        subchild.set('name', 'forceCompile')
        subchild.set('value', 'true')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'cobolbuild')
        child.set('depends', 'init,init.New_Configuration')
        subchild = SubElement(child, 'antcall')
        subchild.set('target', 'pre.build.${cfgtarget}')
        subchild.set('inheritAll', 'true')
        subchild = SubElement(child, 'antcall')
        subchild.set('target', 'cobol.${cfgtarget}')
        subchild.set('inheritAll', 'true')
        subchild = SubElement(child, 'antcall')
        subchild.set('target', 'post.build.${cfgtarget}')
        subchild.set('inheritAll', 'true')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'compileNoBms')
        subchild = SubElement(child, 'antcall')
        subchild.set('target', '${cfg}.FileCompile')
        subchild.set('inheritAll', 'true')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'compile')
        child.set('depends', 'compileNoBms')
    
        child = SubElement(self.top, 'target')
        child.set('name', 'clean')
        child.set('depends', 'init,init.New_Configuration')
        subchild = SubElement(child, 'antcall')
        subchild.set('target', 'clean.${cfgtarget}')
        subchild.set('inheritAll', 'true')        
    def set_dependencies(self, pco):
        """
        Create the dependency with copybooks and pco files
        """
        comment = Comment('****************** Targets for incremental build ******************')
        self.top.append(comment)
        
        child = SubElement(self.top, 'target')
        child.set('name', pco.get_filename())
        child1 = SubElement(child, 'outofdate')
        child2 = SubElement(child1, 'sourcefiles')
     
        child3 = SubElement(child2, 'filelist')    
        child3.set('dir', '${basedir}/'+ pco.get_filepath())
        child3.set('files', pco.get_filename() +'.pco')
    
        for copyobj, path in pco.get_copys().items():
            child3 = SubElement(child2, 'filelist')    
            child3.set('dir', '${basedir}/'+ path)
            child3.set('files', copyobj)
                
        child4 = SubElement(child1, 'targetfiles')
        
        child4.set('path', '${basedir}/New_Configuration.bin/'+ pco.get_filename() +'.o')
        child5 = SubElement(child1, 'sequential')
       
        child6 = SubElement(child5, 'property')   
        child6.set('name', 'filesList')  
        child6.set('value', '${basedir}/'+ pco.get_filepath() + '/' + pco.get_filename() + '.pco')        
     
        child7 = SubElement(child5, 'property')    
        child7.set('name', 'forceCompile')
        child7.set('value', 'true')
    
        child7 = SubElement(child5, 'property')    
        child7.set('name', 'verbose')
        child7.set('value', 'true')     
       
        child8 = SubElement(child5, 'antcall')   
        child8.set('inheritAll', 'true') 
        child8.set('target', 'New_Configuration.FileCompile')
        child9 = SubElement(child8, 'param')
        child9.set('name',  'filesList')
        child9.set('value', '${basedir}/'+ pco.get_filepath() + '/' + pco.get_filename() + '.pco')       
    def set_increment_build(self, pco_objects):
        """
        List all dependencies that needs to checked
        """
        child = SubElement(self.top, 'target')
        child.set('name', 'inc-build')
        all_modules = ''
        for pco in pco_objects:
            all_modules += pco.get_filename() + ','
        
        # remove last comma        
        child.set('depends', all_modules[:-1])   
    def save_2_file(self):        
        """ Save everything to a file"""
        with open(self.buildfile,'wb') as fw:
            fw.write(prettify(self.top))    

                  
class BuildBuildFile(object):
    def __init__(self, buildfile, pco_files):
        
        self.buildfile = BuildFile(buildfile) 
        self.pco_files=pco_files      
        
    def buildbuildfile(self):
 
        self.buildfile.set_project()

        self.buildfile.set_taskdefs()
    
        self.buildfile.set_os_spec_init()
        
        self.buildfile.set_cobol_compiler_directives()
        
        self.buildfile.set_cobol_source_files_header()
        for pco in self.pco_files:
            self.buildfile.set_cobol_source_files(pco.get_filename(), pco.get_filepath()) 
            
        self.buildfile.set_object_files_header()       
        for pco in self.pco_files:
            self.buildfile.set_object_files(pco.get_filename())   
            
        self.buildfile.set_configuration_targets_header()
        for pco in self.pco_files:
            self.buildfile.set_configuration_targets(pco.get_filename())
        self.buildfile.set_configuration_targets_end()
           
        self.buildfile.set_general_targets()   
                       
        for pco in self.pco_files:
             self.buildfile.set_dependencies(pco)
             
        self.buildfile.set_increment_build(self.pco_files)

        self.buildfile.save_2_file()   
        
        
        

def set_project(top):
    """
    Okey, this is the top of the build file ...
    """
    top.set('name', 'src')
    top.set('default', 'cobolbuild')
    top.set('basedir', '.')
    top.set('xmlns:ac', 'antlib:net.sf.antcontrib')
    comment = Comment('Generated for Bolagsverket ab!')
    top.append(comment)
    
#--------------------------------------------------------------------
def set_taskdefs(top):
    """
    Include stuff from MicroFocus to be able to invoke compiler linker and so on...
    """
    child = SubElement(top, 'taskdef')

    child.set('name', 'cobol')
    child.set('classname', 'com.microfocus.ant.TaskCobol')

    echo_message(top, 'Bolagsverkets dynamic buildfile')

    child = SubElement(top, 'taskdef')
    child.set('name', 'cobolclean')
    child.set('classname', 'com.microfocus.ant.TaskCobolClean')

    child = SubElement(top, 'taskdef')
    child.set('name', 'cobollink')
    child.set('classname', 'com.microfocus.ant.TaskCobolLink')

    child = SubElement(top, 'taskdef')
    child.set('uri', 'antlib:net.sf.antcontrib')
    child.set('resource', 'net/sf/antcontrib/antlib.xml')
    child.set('classpath', 'lib/ant-contrib-1.0b3.jar')

    child = SubElement(top, 'typedef')
    child.set('name', 'mfdestfilelist')
    child.set('classname', 'com.microfocus.ant.TypeDestinationFileList')

    child = SubElement(top, 'typedef')
    child.set('name', 'mffilelist')
    child.set('classname', 'com.microfocus.ant.TypeFileList')

    child = SubElement(top, 'typedef')
    child.set('name', 'mfdirlist')
    child.set('classname', 'com.microfocus.ant.TypeDirectiveList')

    child = SubElement(top, 'taskdef')
    child.set('resource', 'net/sf/antcontrib/antcontrib.properties')

#--------------------------------------------------------------------
def set_os_spec_init(top):
    """
    Okey we running linux/unix here
    """
    child = SubElement(top, 'target')
    child.set('name', 'os.init')

    subchild = SubElement(child, 'condition')
    subchild.set('property', 'unix')
    
    subsubchild = SubElement(subchild, 'os')
    subsubchild.set('family', 'unix')

    child = SubElement(top, 'target')
    child.set('name', 'os.init.unix')
    child.set('if', 'unix')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'ddlext')
    subchild.set('value', '.so')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'exeext')
    subchild.set('value', '')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'objext')
    subchild.set('value', '.o')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'equalsInDir')
    subchild.set('value', '=')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'pathVar')
    subchild.set('value', ':')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'shell')
    subchild.set('value', 'sh')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'shell.ext')
    subchild.set('value', '.sh')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'shell.arg')
    subchild.set('value', '-c')

    subchild = SubElement(child, 'property')
    subchild.set('name', 'script header')
    subchild.set('value', '#!/bin/sh')
     
#--------------------------------------------------------------------
def set_cobol_compiler_directives(top):
    """
    Add som ordinary compiler directives
    """
    child = SubElement(top, 'mfdirlist')
    child.set('id', 'cobol_directive_set_1')

    subchild = SubElement(child, 'directive')
    subchild.set('name', 'DIALECT')
    subchild.set('value', 'MF')

    subchild = SubElement(child, 'directive')
    subchild.set('name', 'SOURCEFORMAT')
    subchild.set('value', 'fixed')

    subchild = SubElement(child, 'directive')
    subchild.set('name', 'CHARSET')
    subchild.set('value', 'ASCII')

    subchild = SubElement(child, 'directive')
    subchild.set('name', 'MAX-ERROR')
    subchild.set('value', '100')

    subchild = SubElement(child, 'directives')
    subchild.set('value', 'COPYEXT"cpy,,"')

    subchild = SubElement(child, 'directives')
    subchild.set('value', 'NOLIST')
    
    subchild = SubElement(child, 'directive')
    subchild.set('name', 'SOURCETABSTOP')
    subchild.set('value', '4')

#--------------------------------------------------------------------
def set_cobol_source_files_header(top):
    """
    Start prepare for the source code files that will be added
    """

    child = SubElement(top, 'mffilelist')
    child.set('id', 'cobol_file_set_1')
    child.set('srcdir', '${basedir}')
    child.set('type', 'srcfile')
    return child
 
#--------------------------------------------------------------------
def set_cobol_source_files(child, module, relpath):
    """
    Source code files ...
    """
 
    child = SubElement(child, 'file')
    child.set('name', module +'.pco')     
    child.set('srcdir', relpath)

#--------------------------------------------------------------------
def set_cobol_copybooks_locations(top):
    """
    Some general stuff about the copybooks
    """
    child = SubElement(top, 'mffilelist')
    child.set('id', 'cobol.copybook.locations')

    child = SubElement(child, 'path')
    child.set('type', 'copybook')
    child.set('name', '${src}')

#--------------------------------------------------------------------
def set_cobol_source_files_and_directives(top, module, workspace, relpath ):
    """
    This core stuff. Called when we ready to compile
    """

    #filepath = workspace + '/' +  relpath + '/' + module +'.pco'
    filepath = workspace +  relpath + '/' + module +'.pco'
        
    child = SubElement(top, 'mfdirlist')
    child.set('id', 'dirset.New_Configuration.'+ filepath )
    child.set('refid', 'cobol_directive_set_1')

    child = SubElement(top, 'mffilelist')
    child.set('refid', 'cobol.copybook.locations')

    child = SubElement(top, 'target')
    child.set('name', 'FileCompile.New_Configuration.'+ filepath )
    child.set('depends', 'init')

    subchild = SubElement(child, 'cobol')
    subchild.set('desttype', 'obj')
    subchild.set('destdir', '${basedir}/New_Configuration.bin')
    subchild.set('forceCompile', '${forceCompile}')
    subchild.set('is64bit', 'true')
    subchild.set('threadedRts', 'true')

    subsubchild = SubElement(subchild, 'mffilelist')
    subsubchild.set('refid', 'cobol.copybook.locations')

    subsubchild = SubElement(subchild, 'mfdirlist')
    subsubchild.set('refid', 'dirset.New_Configuration.${filename}')

    subsubchild = SubElement(subchild, 'mffilelist')
    subsubchild.set('srcdir', '${basedir}')
    subsubchild.set('type', 'srcfile')

    subsubsubchild = SubElement(subsubchild, 'file')
    subsubsubchild.set('name', '${filename}')

    subchild = SubElement(child, 'basename')
    subchild.set('property', 'basename')
    subchild.set('file', '${filename}')
    subchild.set('suffix', 'pco')

    subchild = SubElement(child, 'cobollink')
    subchild.set('destdir', '${basedir}/New_Configuration.bin')
    subchild.set('destfile', '${basename}')
    subchild.set('desttype', 'dll/cso')
    subchild.set('entrypoint', '')
    subchild.set('threadedRts', 'true')
    subchild.set('is64bit', 'true')
    subchild.set('objectdir', '${basedir}/New_Configuration.bin')
    subchild.set('debug', 'true')
    subchild.set('objectfile', '${basename}${objext}')

#--------------------------------------------------------------------
def set_object_files_header(top):
    """
    Something about object files
    """
    child = SubElement(top, 'mffilelist')
    child.set('id', 'cobol.default.object.files')
    child.set('srcdir', '${basedir}/${cfgtargetdir}')
    child.set('type', 'objfile')
    return child

#--------------------------------------------------------------------
def set_object_files(child, module):

    subchild = SubElement(child, 'file')
    subchild.set('name', module + '${objext}')

#--------------------------------------------------------------------
def set_configuration_targets_header(top):
    """
    """
    child = SubElement(top, 'target')
    child.set('name', 'cobol.cfg.New_Configuration')
    child.set('depends', 'init')

    subchild = SubElement(child, 'cobol')
    subchild.set('desttype', 'obj')
    subchild.set('destdir', '${basedir}/New_Configuration.bin')
    subchild.set('forceCompile', '${forceCompile}')
    subchild.set('is64bit', 'true')
    subchild.set('threadedRts', 'true')

    subsubchild = SubElement(subchild, 'mffilelist')
    subsubchild.set('refid', 'cobol.copybook.locations')

    subsubchild = SubElement(subchild, 'mfdirlist')
    subsubchild.set('refid', 'cobol_directive_set_1')

    subsubchild = SubElement(subchild, 'mffilelist')
    subsubchild.set('refid', 'cobol_file_set_1')
    return child

#--------------------------------------------------------------------
def set_configuration_targets(child, module):
    """
    """
    subchild = SubElement(child, 'cobollink')
    subchild.set('destdir', '${basedir}/New_Configuration.bin')
    subchild.set('destfile', module)
    subchild.set('desttype', 'dll/cso')
    subchild.set('entrypoint', '')
    subchild.set('threadedRts', 'true')
    subchild.set('is64bit', 'true')
    subchild.set('objectdir', '${basedir}/New_Configuration.bin')
    subchild.set('objectfile', module + '${objext}')

#--------------------------------------------------------------------
def set_configuration_targets_end(top):
    """
    """
    child = SubElement(top, 'target')
    child.set('name', 'New_Configuration.FileCompile')
    child.set('depends', 'init')
    subchild = SubElement(child, 'ac:for')
    subchild.set('list', '${filesList}')
    subchild.set('param', 'filename')
    subchild.set('keepgoing', 'true')
    subchild.set('trim', 'true')
    subchild2 = SubElement(subchild, 'sequential')
    subchild3 = SubElement(subchild2, 'ac:if')
    subchild4 = SubElement(subchild3, 'not')
    subchild5 = SubElement(subchild4, 'isset')
    subchild5.set('property', 'isCancelled')
    subchild6 = SubElement(subchild3, 'then')
    subchild7 = SubElement(subchild6, 'ac:antcallback')
    subchild7.set('target', 'FileCompile.New_Configuration.@{filename}')
    subchild7.set('inheritAll', 'true')
    subchild7.set('return', 'isCancelled')
    subchild8 = SubElement(subchild7, 'param')
    subchild8.set('name', 'filename')
    subchild8.set('value', '@{filename}')

    child = SubElement(top, 'target')
    child.set('name', 'clean.cfg.New_Configuration')
    child.set('depends', 'init')
    child1 = SubElement(child, 'cobolclean')
    child1.set('desttype', 'dll')
    child1.set('destdir', '${basedir}/New_Configuration.bin')
    child1.set('debug', 'true')
    child2 = SubElement(child1, 'mffilelist')
    child2.set('refid', 'cobol_file_set_1')

    child = SubElement(top, 'target')
    child.set('name', 'pre.build.cfg.New_Configuration')
    child.set('depends', 'init')

    child = SubElement(top, 'target')
    child.set('name', 'post.build.cfg.New_Configuration')
    child.set('depends', 'init')

#--------------------------------------------------------------------
def set_general_targets(top):
    """
    """
    child = SubElement(top, 'target')
    child.set('name', 'init.New_Configuration')
    subchild = SubElement(child, 'property')
    subchild.set('name', 'cfgtargetdir')
    subchild.set('value', 'New_Configuration.bin')

    child = SubElement(top, 'target')
    child.set('name', 'init')
    child.set('depends', 'os.init, os.init.unix')
    subchild = SubElement(child, 'property')
    subchild.set('environment', 'env')
    subchild = SubElement(child, 'property')
    subchild.set('name', 'src')
    subchild.set('value', '${basedir}')
    subchild = SubElement(child, 'property')
    subchild.set('name', 'cfg')
    subchild.set('value', 'New_Configuration')
    subchild = SubElement(child, 'property')
    subchild.set('name', 'cfgtarget')
    subchild.set('value', 'cfg.${cfg}')
    subchild = SubElement(child, 'property')
    subchild.set('name', 'forceCompile')
    subchild.set('value', 'true')

    child = SubElement(top, 'target')
    child.set('name', 'cobolbuild')
    child.set('depends', 'init,init.New_Configuration')
    subchild = SubElement(child, 'antcall')
    subchild.set('target', 'pre.build.${cfgtarget}')
    subchild.set('inheritAll', 'true')
    subchild = SubElement(child, 'antcall')
    subchild.set('target', 'cobol.${cfgtarget}')
    subchild.set('inheritAll', 'true')
    subchild = SubElement(child, 'antcall')
    subchild.set('target', 'post.build.${cfgtarget}')
    subchild.set('inheritAll', 'true')

    child = SubElement(top, 'target')
    child.set('name', 'compileNoBms')
    subchild = SubElement(child, 'antcall')
    subchild.set('target', '${cfg}.FileCompile')
    subchild.set('inheritAll', 'true')

    child = SubElement(top, 'target')
    child.set('name', 'compile')
    child.set('depends', 'compileNoBms')

    child = SubElement(top, 'target')
    child.set('name', 'clean')
    child.set('depends', 'init,init.New_Configuration')
    subchild = SubElement(child, 'antcall')
    subchild.set('target', 'clean.${cfgtarget}')
    subchild.set('inheritAll', 'true')

#--------------------------------------------------------------------
def set_dependencies(top, pco):
    """
    Create the dependency with copybooks and pco files
    """
    child = SubElement(top, 'target')
    child.set('name', pco.get_filename())
    child1 = SubElement(child, 'outofdate')
    child2 = SubElement(child1, 'sourcefiles')
 
    child3 = SubElement(child2, 'filelist')    
    child3.set('dir', '${basedir}/'+ pco.get_filepath())
    child3.set('files', pco.get_filename() +'.pco')

    for copyobj, path in pco.get_copys().items():
        child3 = SubElement(child2, 'filelist')    
        child3.set('dir', '${basedir}/'+ path)
        child3.set('files', copyobj)
            
    child4 = SubElement(child1, 'targetfiles')
    
    child4.set('path', '${basedir}/New_Configuration.bin/'+ pco.get_filename() +'.o')
    child5 = SubElement(child1, 'sequential')
   
    child6 = SubElement(child5, 'property')   
    child6.set('name', 'filesList')  
    child6.set('value', '${basedir}/'+ pco.get_filepath() + '/' + pco.get_filename() + '.pco')        
 
    child7 = SubElement(child5, 'property')    
    child7.set('name', 'forceCompile')
    child7.set('value', 'true')

    child7 = SubElement(child5, 'property')    
    child7.set('name', 'verbose')
    child7.set('value', 'true')     
   
    child8 = SubElement(child5, 'antcall')   
    child8.set('inheritAll', 'true') 
    child8.set('target', 'New_Configuration.FileCompile')
    child9 = SubElement(child8, 'param')
    child9.set('name',  'filesList')
    child9.set('value', '${basedir}/'+ pco.get_filepath() + '/' + pco.get_filename() + '.pco')     

def set_increment_build(top, pco_objects):
    """
    List all dependencies that needs to checked
    """
    child = SubElement(top, 'target')
    child.set('name', 'inc-build')
    all_modules = ''
    for pco in pco_objects:
        all_modules += pco.get_filename() + ','
    
    # remove last comma        
    child.set('depends', all_modules[:-1])       
 
    
#--------------------------------------------------------------------
def main(args):

    if len(args) != 3:
        print 'Missing arguments'
        return 1 

    JenkinsWorkspace = args[0]
    workSpace = JenkinsWorkspace + '/src/'
    #workSpace2 = JenkinsWorkspace + '/src'
    buildFile = args[1]
    pickleFile = args[2]
 

    """Create a list of pco objects """  
    pcobuilder = PcoBuilder(workSpace)

    """ Create a pickle file to be able to single compile in Jenkins """
    absolute_dict = dict()
    for pco in pcobuilder.pco_files:
        absolute_dict[pco.get_filename()] = workSpace + pco.get_filepath() + '/' + pco.get_filename() + '.pco'
        
    write_dict_2_file(absolute_dict, pickleFile)    
    
    
    #buildfilebuilder = BuildBuildFile(buildFile, pcobuilder.pco_files)
    
    #buildfilebuilder.buildbuildfile()
    # return 0
    
    """Create a dynamic build file """    

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
  
    for pco in pcobuilder.pco_files:
        set_cobol_source_files(child, module=pco.get_filename(), relpath=pco.get_filepath())    
    
    comment = Comment('****************** COBOL copybook locations ******************')
    top.append(comment)
    set_cobol_copybooks_locations(top)

    comment = Comment('****************** COBOL Source Files and Directive Set ******************')
    top.append(comment)
  
    for pco in pcobuilder.pco_files:
        set_cobol_source_files_and_directives(top, pco.get_filename(), workSpace, pco.get_filepath())
        
    comment = Comment('****************** Object files ******************')
    top.append(comment)

    child = set_object_files_header(top)
        
    for pco in pcobuilder.pco_files:
        set_object_files(child, pco.get_filename())    

    comment = Comment('****************** Configuration targets ******************')
    top.append(comment)
    child = set_configuration_targets_header(top)
   
    for pco in pcobuilder.pco_files:
        set_configuration_targets(child, pco.get_filename())

    set_configuration_targets_end(top)

    comment = Comment('****************** General targets ******************')
    top.append(comment)
    set_general_targets(top)


    comment = Comment('****************** Targets for incremental build ******************')
    top.append(comment)
       
    """Generate dependency targets for every pco """
    for pco in pcobuilder.pco_files:
        set_dependencies(top, pco)
    
    """ Add all targets for incremental build """
    set_increment_build(top, pcobuilder.pco_files)
    
    """ Save everything to a file"""
    with open(buildFile,'wb') as fw:
        fw.write(prettify(top))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))



