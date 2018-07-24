#!/bin/bash 

HASH=${1}

echo "docker run --rm \
  --mount type=bind,source=${PWD}/binutils,target=/install \
  --mount type=bind,source=/home/andrew/code/binutils-gdb,target=/code,readonly \
  --mount type=bind,source=/home/andrew/code/build-all-binutils,target=/utils \
  buildbinutils \
  /utils/buildit.sh $HASH"
