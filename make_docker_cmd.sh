#!/bin/bash 

HASH=${1}

echo "docker run --rm \
  --mount type=bind,source=/data/backup/binutils/$HASH,target=/install \
  --mount type=bind,source=/home/andrew/code/binutils-gdb-bare,target=/code,readonly \
  --mount type=bind,source=/home/andrew/code/build-all-binutils,target=/utils \
  buildbinutils \
  /utils/buildit.sh $HASH"
