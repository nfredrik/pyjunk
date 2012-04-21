
###############################################################
# 
# This is a conditionally nightly build, i.e. every
# midnight we will check if there has is been any updating on
# trunk,  if so there will be an build
#
# Short description:
# The job will save the subversion global number in an
# file before doing an update/check out on the trunk 
# If the new global subversion number is higher than the
# one saved on file we will do an build.
#
#
# Build Envirnoment -> 
# Run buildstep before SCM runs ->
# execute shell
#
#
###############################################################

OK=0
ERROR=42
TMPFILESVN='/tmp/svn_old_global_rev_no'

##################################################
# TODO change these variables to the correct ones
##################################################
SUBVERSION_1=40

echo $SUBVERSION_1 > $TMPFILESVN

# Check that the file could be created, if not
# mark as failure and make sure that someone is emailed!
if [[ ! -e $TMPFILESVN ]]; then
    echo "could not create: ${TMPFILESVN}"
    exit $ERROR
fi

###############################################################
#
# Build -> execute shell
#
###############################################################

OK=0
ERROR=42
TMPFILESVN='/tmp/svn_old_global_rev_no'

# Check that the file exist and not empty, otherwise
# regard the build as a failure
if [[ ! -e $TMPFILESVN && ! -s $TMPFILESVN ]]; then
    echo "${TMPFILESVN} do not exist or is empty!"
    exit $ERROR
fi

# Read the current version of subversion global version number
# from our file created earlier in this build
SVN_OLD_GLOBAL_REV_NO=`cat ${TMPFILESVN}`

# Check that it's a numeral, otherwise exit!
if [[ !  $(echo "$SVN_OLD_GLOBAL_REV_NO" | grep -E "^[0-9]+$") ]]
then
    echo "not an valid integer : ${SVN_OLD_GLOBAL_REV_NO}"
    exit $ERROR
fi

##################################################
# TODO change these variables to the correct ones
##################################################
SUBVERSION_1=43
SVN_NEW_GLOBAL_REV_NO=$SUBVERSION_1


# If current version, SVN_NEW_GLOBAL_REV_NO is equal no build
# will be launched, just exit gracefully
if [[    $SVN_NEW_GLOBAL_REV_NO  == $SVN_OLD_GLOBAL_REV_NO  ]]; then
    echo "Nothing has happened since last night quit!"
    echo "old :${SVN_OLD_GLOBAL_REV_NO} new :${SVN_NEW_GLOBAL_REV_NO}"
    exit $OK
fi

# This should never happen, if exit hard!
if (($SVN_NEW_GLOBAL_REV_NO  < $SVN_OLD_GLOBAL_REV_NO)) ; then
    echo "Something is totally wrong here, old higher value than new!"
    echo "old ${SVN_OLD_GLOBAL_REV_NO} new: ${SVN_NEW_GLOBAL_REV_NO}"
    exit $ERROR
fi

# Everyting is okey, start the build
echo "We have an updated version:  ${SVN_NEW_GLOBAL_REV_NO}, start build"
