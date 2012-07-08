#!/usr/bin/env sh

echo 'hej'

#
# TODO:
# Should following sqlscript be commited to databas: UTV100?
# Answer yes or no!
# 
# Logging of all actions? with wrapping logs?
# path to logfile in config file?
#
# Check for empty sqlscript!
# 
# Check if sqlplus is executable
#
# Check if database is up and running!
#
# Verify that from config file variables are none empty!
#


echo "Reading config ..." >&2

source ./database.cfg
echo "Config for NISSE: $NISSE"
echo "Config for JANNE: $JANNE"
echo "Config for TOM: $TOM"
echo "Config for TOMA: $TOMA"

if [[ $NISSE != "" ]];
then
   echo 'nisse  defined'
fi

# Chapter 48.05
case "${NISSE+X}" in

X)
    echo "Hurra"
    ;;
*) 
    echo "Noo"
    ;;
esac
