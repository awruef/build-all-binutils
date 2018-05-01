# Steps 

1. Create a docker image of Ubuntu 14.04, that Ubuntu image installs the 
   following packages: `g++ gcc automake autoconf m4 flex bison git build-essential`
2. Create a script, `buildit.sh` that does the following:
  1. Does a `git clone` from `/code` into `/build` 
  2. Does a `git checkout` of a specific hash, `<HASH>`, as a parameter. 
  3. Does a `./configure --prefix /install`
  4. Does a `make install` 
3. Create a wrapper script that builds up command lines to invoke docker around
   `buildit.sh` but with the following variables: 
   1. bind-mount /home/andrew/code/binutils-gdb-bare to /code
   2. bind-mount /home/andrew/built_binutils/<HASH> to /install
   3. bind-mount /home/andrew/code/build-all-binutils to /utils

   This script will output a call to docker, and run `/utils/buildit.sh <HASH>`
4. Create a final script that iterates over a list of commits as hashes and 
   calls `make_docker_cmd.sh` on each, while also doing a 
   `mkdir /home/andrew/built_binutils/<HASH>`
5. Feed the output of that script to `parallel` and wait.
