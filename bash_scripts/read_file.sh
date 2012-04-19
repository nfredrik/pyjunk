
###############################################################
# before build
###############################################################

OK=0
ERROR=42

set +x

# pre check out
# simulate the old value
SUBVERSION_1=40


echo $SUBVERSION_1 > ./svn_old_global_rev_no

# Check that the file could be created, if not email to admin!
if [[ ! -e ./svn_old_global_rev_no ]]; then
    echo "could not create: svn_old_global_rev_no"
    exit $ERROR
fi


###############################################################
# at build
###############################################################

OK=0
ERROR=42


# Check that the file exist, if not email to admin!
if [[ ! -e ./svn_old_global_rev_no ]]; then
    echo "svn_old_global_rev_no do not exist!"
    exit $ERROR
fi


# Read the current version of subversion global version number
# before checkout
SVN_OLD_GLOBAL_REV_NO=`cat ./svn_old_global_rev_no`


SUBVERSION_1=43
SVN_NEW_GLOBAL_REV_NO=$SUBVERSION_1


# If current version, NEWSWN is equal or less than 
# new checkout version, terminate
# if [[ ! $SVN_NEW_GLOBAL_REV_NO -gt $SVN_OLD_GLOBAL_REV_NO  ]]; then    this works!!!
if [[    $SVN_NEW_GLOBAL_REV_NO  == $SVN_OLD_GLOBAL_REV_NO  ]]; then
    echo "Nothing has happened since last night quit!"
    echo "old :${SVN_OLD_GLOBAL_REV_NO} new :${SVN_NEW_GLOBAL_REV_NO}"
    exit $OK
fi

if (($SVN_NEW_GLOBAL_REV_NO  <= $SVN_OLD_GLOBAL_REV_NO)) ; then
    echo "Something is totally wrong here, old higher value than new!"
    echo "old ${SVN_OLD_GLOBAL_REV_NO} new: ${SVN_NEW_GLOBAL_REV_NO}"
    exit $ERROR
fi

echo "We have an updated version to build: ${SVN_NEW_GLOBAL_REV_NO}, start build"

exit $OK