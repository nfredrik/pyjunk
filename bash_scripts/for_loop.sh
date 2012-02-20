#!/bin/bash 
#set -x

index=190

for i in fsv jel mad mth
do
   echo $i $index
   let "index+=1"
done