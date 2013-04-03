#!/usr/bin/env sh

#while sleep 5
while sleep 0.1
do
  echo -e "===== $(date) ====="
  ls status.log
done > status.log
