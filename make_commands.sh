#!/bin/bash
set -e

COMMITS=${1}

cat $COMMITS |
while read i; do
  ./make_docker_cmd.sh $i 
done
