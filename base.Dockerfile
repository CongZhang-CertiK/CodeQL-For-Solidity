# Copyright 2023 CertiK
# This code is proprietary and not licensed. It is intended for internal use at CertiK only.
# Author: Ju Chen (ju.chen@certik.com)
# Base docker image installed with necessary packages.

FROM ubuntu:rolling

RUN apt-get update -y

# paresol environment
RUN apt-get install -y opam
RUN opam init -c 4.14.1 -y --disable-sandboxing
RUN eval $(opam env --switch=4.14.1)

# auto-build environment
# RUN echo "deb http://mirrors.aliyun.com/ubuntu/ $(lsb_release -cs) main restricted universe multiverse" | tee /etc/apt/sources.list && apt-get update
# RUN echo "deb http://mirrors.aliyun.com/ubuntu/ $(awk -F= '/^VERSION_CODENAME=/{print $2}' /etc/os-release) main restricted universe multiverse" | tee /etc/apt/sources.list && apt-get update
RUN apt-get install -y node.js npm python3-pip time curl
RUN npm install -g truffle yarn
