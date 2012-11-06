#!/usr/bin/env bash

#
# Script to detect if there has been any changes in the subversion repository,
# i.e only pgm directory.

set -x

# Define exit codes and URL to repository
OK=0
ERROR=42
URL='https://subversion01/repos/uniregrepos/branches/utveckling/pgm'

# Get _dates_ for day before yesterday and yesterday
DAY_BEFORE_YESTERDAY=`(date --date='2 days ago' +"%Y-%m-%d" )`
INPUT_YESTERDAY=`(date --date='1 days ago' +"%Y-%m-%d" )`

# Get the latest _revisions_ from day before yesterday and yesterday
BEFORE_YESTERDAY=`svn info -r \{$DAY_BEFORE_YESTERDAY\} $URL |grep "Last Changed Rev"| awk '{print $4}'`
YESTERDAY=`svn info -r \{$INPUT_YESTERDAY\} $URL |grep "Last Changed Rev"| awk '{print $4}'`


# Check that it's a numeral, otherwise exit!
if [[ !  $(echo "$BEFORE_YESTERDAY" | grep -E "^[0-9]+$") ]]
then
    echo "not an valid numeral : ${BEFORE_YESTERDAY}"
    exit $ERROR
fi

# Same here
if [[ !  $(echo "$YESTERDAY" | grep -E "^[0-9]+$") ]]
then
    echo "not an valid numeral : ${YESTERDAY}"
    exit $ERROR
fi

# If version are equal no build will be launched, just exit
if [[ $BEFORE_YESTERDAY == $YESTERDAY ]]; then
    echo "Nothing has happened since last night quit!"
    echo "day before yesterday : ${BEFORE_YESTERDAY} yesterday : ${YESTERDAY}"
    exit $ERROR
fi

# This should never happen, if exit!
if (($YESTERDAY < $BEFORE_YESTERDAY)) ; then
    echo "Something is totally wrong here, old higher value than new!"
    echo "day before yesterday : ${BEFORE_YESTERDAY} yesterday : ${YESTERDAY}"
    exit $ERROR
fi

# Everything is okey, start the build
echo "It is time to build! day before yesterday: ${BEFORE_YESTERDAY}, yesterday: ${YESTERDAY} , start build"
