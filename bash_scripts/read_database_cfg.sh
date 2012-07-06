#!/usr/bin/env sh

echo 'hej'

echo "Reading config ..." >&2

source ./database.cfg
echo "Config for NISSE: $NISSE"
echo "Config for JANNE: $JANNE"
echo "Config for TOM: $TOM"
echo "Config for TOMA: $TOMA"

if [[ $NISSE != "" ]];
then
   echo 'nisse not defined'
fi