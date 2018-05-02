#!/bin/bash
set -e

COMMITS=${1}

cat $COMMITS |
while read i; do
  mkdir /data/backup/binutils/$i
  ./make_docker_cmd.sh $i >> commands.par
done
