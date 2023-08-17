# Copyright 2023 CertiK
# This code is proprietary and not licensed. It is intended for internal use at CertiK only.
# Author: Ju Chen (ju.chen@certik.com)
# Modified by: Cong Zhang(cong.zhang@certik.com)
# Docker image for the version of paresol undertest

ARG ocaml_solidity_version
ARG paresol_version
FROM paresol_testing_${ocaml_solidity_version}_${paresol_version}

WORKDIR /workdir
COPY transform.py /workdir
COPY runner.py /workdir
COPY triage.py /workdir
