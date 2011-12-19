#/usr/bin/sh 

#set -x

name=kalle
name1="kalle kula"
name2="$name kula"

echo han heter $name2


## second statement executes IF first statement went well (true)
(ls | grep pipes_ands.sh > /dev/null) && echo $0 finns 


## second statement executes IF first statement went wrong (false)
(ls | grep nisse > /dev/null) || echo nisse finns inte 


