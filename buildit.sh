#!/bin/bash

HASH=${1}

git clone /code /build 
cd /build 
git checkout $HASH 
./configure --prefix /install 
make install 
