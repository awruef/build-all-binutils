#!/bin/bash 

HASH=${1}

echo "docker run --rm -ti \
  --mount type=bind,source=/home/andrew/built_binutils/$HASH,target=/install \
  --mount type=bind,source=/home/andrew/code/binutils-gdb-bare,target=/code \
  --mount type=bind,source=/home/andrew/code/build-all-binutils,target=/utils \
  buildbinutils \
  /utils/builtit.sh $HASH"
