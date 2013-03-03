#!/usr/bin/env sh

assert ()                 #  If condition false,
{                         #+ exit from script
                          #+ with appropriate error message.
    E_PARAM_ERR=98
    E_ASSERT_FAILED=99


    if [ -z "$2" ]          #  Not enough parameters passed
    then                    #+ to assert() function.
        return $E_PARAM_ERR   #  No damage done.
    fi

    lineno=$2

    #echo 'assert first arg:' $1
    if [ ! $1 ] 
    then
      echo "Assertion failed:  \"$1\""
      echo "File \"$0\", line $lineno"    # Give name of file and line number.
      exit $E_ASSERT_FAILED
    fi  
}

assert "5 -lt 6" $LINENO

ls *.txtff &> /dev/null

assert "$? -eq 0" $LINENO



echo 'hi!'

if ls *.pym &> /dev/null ; then
    echo 'Yes'
    
fi
