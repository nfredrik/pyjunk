#!/usr/bin/env bash

echo 5

set -x
cd tables/tests/steps
python test_tables.py

cd -

behave tables/tests  --no-capture