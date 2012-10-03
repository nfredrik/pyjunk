#!/usr/bin/sh 

#set -x

echo '---------------------------------'
echo 'args and builtin variables'
echo '---------------------------------'

echo 'number of args:' $#
echo 'options in effext:' $-
echo 'all args:' $*
echo 'all args in serie:' $@
echo 'exit status of last command:' $?
echo 'PID of this shell process:' $$
echo 'PID of last last bakground job:' $!
echo 'name of script:' $0

echo '---------------------------------'
echo 'Conditional variable substitution'
echo '---------------------------------'
var1='var1 set'
echo ${var1:-'var1 not set now'}



#var2='var2 set'
echo ${var2:='var2 set now'}
echo $var2 'after'

#var3='var3 set'
echo ${var3:?'var3 never set exit'}

${var4:+string}
