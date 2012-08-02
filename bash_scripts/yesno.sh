#!/usr/bin/env bash

#
# TODO what about  echo -n ???
# trap
#

#trap 'echo "`basename $0`: Ouch! Quitting early." 1>2&' 1 2 15
#trap 'echo you hit Ctrl-C, no commit executed...; exit' SIGINT SIGQUIT
trap 'myExit; exit 42' SIGINT SIGQUIT


myExit()
{
    echo ' You hit Ctrl-C, No commit to' ${DB} 'executed...'
}

SCRIPT=nisse.sql
DB=UTV100

while true
do
  echo -n  'Do you want' $SCRIPT 'to be commited to: ' $DB ' ? [Y/n] '

  read CONFIRM
  case $CONFIRM in
    y|Y|'') break ;;
    n|N)
      echo 'You declined. No commit to:' $DB ' done'
      exit 42
      ;;
    *) echo "That is not vaild input. Try again!"
  esac
done

echo 'committed'