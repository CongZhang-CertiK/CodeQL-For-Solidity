# Copyright 2023 CertiK
# This code is proprietary and not licensed. It is intended for internal use at CertiK only.
# Author: Ju Chen (ju.chen@certik.com)
# Docker image for the version of paresol undertest
# FIXME: let user specifiy the version of paresol for testing

FROM paresol_testing_base
ARG ocaml_solidity_version
ARG paresol_version

WORKDIR /workdir
RUN apt-get install -y libgmp-dev
RUN apt-get install -y virtualenv
COPY ocaml-solidity-internal /workdir/ocaml-solidity-internal
COPY paresol /workdir/paresol
COPY auto-build /workdir/auto-build
RUN cd /workdir/auto-build && virtualenv env && . env/bin/activate && ./install-dependencies.sh
RUN cd ocaml-solidity-internal && git checkout $ocaml_solidity_version && \
    eval $(opam env --switch=4.14.1) && \
    opam install -y visitors && \
    opam install . -y
RUN cd /workdir/paresol && git checkout $paresol_version && \
    eval $(opam env --switch=4.14.1) && \
    opam install -y logs && \
    dune build
ENV PATH=/workdir/paresol/_build/install/default/bin:${PATH}
RUN npm install -g --prefix=npm_modules solidity-bytes-utils
RUN npm install -g --prefix=npm_modules @openzeppelin/contracts-upgradeable@4.7
RUN npm install -g --prefix=npm_modules @openzeppelin/contracts@4.7
RUN npm install -g --prefix=npm_modules @chainlink/contracts
RUN npm install -g --prefix=npm_modules hardhat
RUN npm install -g --prefix=npm_modules solady 
RUN npm install -g --prefix=npm_modules @uniswap/v2-periphery
RUN npm install -g --prefix=npm_modules @uniswap/v2-core
RUN mkdir /workdir/output
