#!/usr/bin/env sh
# TODO:
# binary files should go under SRPMS
# check afterwards in this script with rpmlint?
# one or several rpms?
# Dependencies?  framework?
# md5?
# installera köra i rpm:en?

# exempel på rpm :    unireg_pgm-d20120114-svn012345-b0023.rpm ???

set -x 

export WORKSPACE=$1
export TAGNAME=$2
export BUILD_NUMBER=$3

cd $WORKSPACE

#[[ -d rpmbuild ]] && rm -fr rpmbuild
#    mkdir rpmbuild
    
#cd rpmbuild

# Clean up and create directories
for dir in BUILD RPMS SOURCES SPECS SRPMS
do
 [[ -d $dir ]] && rm -Rf $dir
  mkdir $dir
done

# Create application file

# echo "echo Hello World" > helloworld.sh 

# Put our files in the right place
mv helloworld.sh SOURCES/.
mv helloworld.spec SPECS/.

# Create rpm in RPMS/noarch/
rpmbuild  --define 'TAGNAME '$TAGNAME  --define 'BUILD_NUMBER '$BUILD_NUMBER --define '_topdir '`pwd` -ba SPECS/helloworld.spec


# rpmlint

NO_OF_RPMS=$(find . -name *.rpm)

for rpm in $NO_OF_RPMS
do
	rpmlint $rpm
	if [[ $? != 0 ]]; then
	    echo 'You did not follow the rpmlint rules!'
	    #exit 42
	fi    
done

