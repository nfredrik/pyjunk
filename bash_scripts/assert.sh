#!/bin/bash
#set -x

#--------------------------------------------------------------
function debug 
{
    if [ $debug ]; then
	echo -e $1
    fi
}

#--------------------------------------------------------------
#
# assert()
#
# Disabled if NDEBUG defined.
#
# Examples, check for result of command: assert "$? -ne 0" "ls on dir directory failed"
#
function assert()
{   

    # If NDEBUG set do not care about assert
    if [ -n "$NDEBUG" ]
    then
        return
    fi

    # Make sure that we have an argument
    if [ -z "$1" ] 
    then
        echo 'assert: argument not set' $1
        exit 42
    fi
              
    # Okey here we are, expression true?
    if [ ! $1 ] 
    then
        echo "Assertion failed:  \"$1\""
        echo 'lineno, function, file:' $(caller 0)
        [ -n "$2" ] && {echo $2}
        exit 42
    fi  
}


cat nisse &>/dev/null

NDEBUG=true

#assert "${?} -eq 0"

a=8
b=4
condition="$a -lt $b"
assert "$condition"
