#!/bin/bash
set -e
HASH=${1}

#git clone /code /build 
cd /build
git checkout $HASH
ASAN_OPTIONS=detect_leaks=0 CC=clang CXX=clang++ ./configure CFLAGS="-fsanitize=address,undefined -Wno-error=null-pointer-arithmetic" CXXFLAGS="-fsanitize=address,undefined -Wno-error=null-pointer-arithmetic" --prefix /install/$HASH --disable-gdb
#CC=clang-3.8 CXX=clang++-3.8 ./configure CFLAGS="-g -ggdb" CXXFLAGS="-g -ggdb" --prefix /install/$HASH --disable-gdb
#make && make install && make clean
ASAN_OPTIONS=detect_leaks=0 make && ASAN_OPTIONS=detect_leaks=0 make install && ASAN_OPTIONS=detect_leaks=0 make clean
find /install/$HASH -type f ! -name c++filt ! -name nm -delete
find /install/$HASH -type d -empty -delete
