#!/bin/bash
# assert.sh
#set -x

#--------------------------------------------------------------
function assert()
{   

    # NDEBUG set do not care about assert
    if [ -n "$NDEBUG" ]
    then
         echo 'NBDEBUG:' $NDEBUG
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
        exit 42
    fi  
}

#--------------------------------------------------------------
function oldassert ()                 #  If condition false,
{                         #+ exit from script
                          #+ with appropriate error message.
  E_PARAM_ERR=98
  E_ASSERT_FAILED=99


  if [ -z "$2" ]          #  Not enough parameters passed
  then                    #+ to assert() function.
    return $E_PARAM_ERR   #  No damage done.
  fi

  lineno=$2
#  echo "---- 1 ar:", $1
  if [ ! $1 ] 
#  if [[ ! -n $1 || ! $1 ]] 
  then
    echo "Assertion failed:  \"$1\""
#    echo "File \"$0\", line $lineno"    # Give name of file and line number.
    echo 'lineno, function, file:' `caller 0`
    exit $E_ASSERT_FAILED
  # else
  #   return
  #   and continue executing the script.
  fi  
} # Insert a similar assert() function into a script you need to debug.    
#--------------------------------------------------------------

#EXITCODE_ZERO='\$\? -eq 0'

#EXITCODE_ZERO=`echo -e ${?} -eq 0`

#EXITCODE_ZERO=$(cat <<EOF 
#${?} -eq 0
#EOF
#)

#echo 'har har du:' $EXITCODE_ZERO ':'

cat nisse &>/dev/null

#NDEBUG=true

assert "${?} -eq 0"
#assert  $EXITCODE_ZERO $LINENO

a=3
b=4
condition="$a -lt $b"     #  Error message and exit from script.
                          #  Try setting "condition" to something else
                          #+ and see what happens.

# assert "$condition" $LINENO
# The remainder of the script executes only if the "assert" does not fail.


# assert " " $LINENO

var=''
# assert $var $LINENO

# Some commands.
# Some more commands . . .

# . . .
# More commands . . .

exit $?
