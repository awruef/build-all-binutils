FROM ubuntu:latest

MAINTAINER Andrew Ruef version: 0.5

COPY binutils-gdb /build

RUN apt-get update && apt-get upgrade -y && apt-get install -y g++ gcc automake autoconf m4 flex bison git build-essential texinfo unzip zip clang
