#!/bin/bash
set -e
HASH=${1}

git clone /code /build > /dev/null
cd /build 
git checkout $HASH > /dev/null
./configure --prefix /install --disable-gdb > /dev/null
make && make install > /dev/null
make clean  > /dev/null
