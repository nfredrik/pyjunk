#!/bin/sh 

set +x

if [ -x $0  ]
then
    echo 'allowed to execute'
else
    echo 'not executable'
fi

SUM=12

while [ $SUM == 12  ]
do
    SUM=11
done 

until [ $SUM == 12  ]
do
    SUM=12
done

var='start'

case "$var" in

'start')
   echo 'starting...'
   ;;
'stop')
   echo 'stopping...'
   ;;
*)
   echo 'no...'
   ;;
esac


for var in  `ls` 
do
    echo "$var"
done