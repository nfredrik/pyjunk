#!/usr/bin/env bash


set -x

export WORKSPACE=$1

cd  $WORKSPACE/src

cp antcobolBuild antcobolBuildtest

echo 'WORKSPACE: ' $WORKSPACE

#sed -i "s/\.[0-9A-Za-z\/]*\(\/src[0-9A-Za-z/\.]*pco\)/\.${WORKSPACE}\1/"  ./antcobolBuildtest
#sed -i 's/\.[0-9A-Za-z\/]*\(\/src[0-9A-Za-z/\.]*pco\)/\.$WORKSPACE\1/'  ./antcobolBuildtest
sed -i "s#\.[0-9A-Za-z\/]*\(\/src[0-9A-Za-z/\.]*pco\)#\.${WORKSPACE}\1#"  ./antcobolBuildtest