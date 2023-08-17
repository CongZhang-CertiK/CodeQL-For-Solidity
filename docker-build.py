#!/usr/bin/env python3
# Copyright 2023 CertiK
# This code is proprietary and not licensed. It is intended for internal use at CertiK only.
# Author: Ju Chen (ju.chen@certik.com)
# Modified by: Cong Zhang(cong.zhang@certik.com)

# Intergrated environment of CodeQL-for-Solidity

import os
import subprocess
import yaml
import shutil
import docker


def check_image_exists(image_name):
    # Create a client object for Docker
    client = docker.from_env()

    # Define the name of the image to check
    image_name = image_name + ':latest'

    # Check if the image is present
    image_list = client.images.list()
    image_tags = [image.attrs['RepoTags'] for image in image_list]
    if image_name in sum(image_tags, []):
        return True
    else:
        return False


def build_base_image(workdir):
    """Docker images hierachy: base image -> target image (with ocaml_solidity and paresol installed
     In this function, we build base image. It raises an exception if anything goes wrong"""
    if check_image_exists('paresol_testing_base'):
        return
    command = [
        'docker',
        'build',
        '-t',
        'paresol_testing_base',
        '--platform',
        'linux/x86_64',
        '-f',
        'base.Dockerfile',
        '.'
    ]
    subprocess.check_call(command, cwd=workdir)


def build_target_image(targets, workdir):
    """Docker images hierachy: base image -> target image (with ocaml_solidity and paresol installed
     In this function, we build target image. It raises an exception if anything goes wrong"""
    for target in targets:
        ocaml_solidity_version = target['ocaml_solidity_version']
        paresol_version = target['paresol_version']
        if check_image_exists('paresol_testing_'+ocaml_solidity_version+'_'+paresol_version):
            continue
        command = [
            'docker',
            'build',
            '-t',
            f'paresol_testing_{ocaml_solidity_version}_{paresol_version}',
            '--platform',
            'linux/x86_64',
            '--build-arg',
            f'ocaml_solidity_version={ocaml_solidity_version}',
            '--build-arg',
            f'paresol_version={paresol_version}',
            '-f',
            'target.Dockerfile',
            '.'
        ]
        subprocess.check_call(command, cwd=workdir)


def build_codeql_image(targets, workdir):
    """Docker images hierachy: base image -> target image (with ocaml_solidity and paresol installed
     In this function, we build target image. It raises an exception if anything goes wrong"""
    for target in targets:
        ocaml_solidity_version = target['ocaml_solidity_version']
        paresol_version = target['paresol_version']
        codeql_version = target['codeql_version']
        if check_image_exists('codeql_build_' + ocaml_solidity_version + '_' + paresol_version + '_' + codeql_version):
            continue
        command = [
            'docker',
            'build',
            '-t',
            f'codeql_build_{ocaml_solidity_version}_{paresol_version}_{codeql_version}',
            '--platform',
            'linux/x86_64',
            '--build-arg',
            f'ocaml_solidity_version={ocaml_solidity_version}',
            '--build-arg',
            f'paresol_version={paresol_version}',
            '--build-arg',
            f'codeql_version={codeql_version}',
            '-f',
            'codeql.Dockerfile',
            '.'
        ]
        subprocess.check_call(command, cwd=workdir)


def setup_environment(workdir):
    """Download code from CertiK internal repos.
    * paresol
    * ocaml-solidity-internal"""
    command_download = [
        'git',
        'clone',
        'git@github.com:certikproject/paresol'
    ]
    command_pull = [
        'git',
        'pull'
    ]

    # paresol
    paresol_path = os.path.join(workdir, 'paresol')
    if not os.path.exists(paresol_path):
        subprocess.check_call(command_download, cwd=workdir)
    else:
        subprocess.check_call(command_pull, cwd=paresol_path)

    # ocaml-solidity-internal
    ocaml_solidity_path = os.path.join(workdir, 'ocaml-solidity-internal')
    command_download[2] = 'git@github.com:certikproject/ocaml-solidity-internal'
    if not os.path.exists(ocaml_solidity_path):
        subprocess.check_call(command_download, cwd=workdir)
    else:
        subprocess.check_call(command_pull, cwd=ocaml_solidity_path)

    # auto-build
    auto_build_path = os.path.join(workdir, 'auto-build')
    command_download[2] = 'git@github.com:certikproject/auto-build'
    if not os.path.exists(auto_build_path):
        subprocess.check_call(command_download, cwd=workdir)
        command = [
            'git',
            'checkout',
            'stable'
        ]
        subprocess.check_call(command, cwd=auto_build_path)
        command = [
            'git',
            'submodule',
            'update',
            '--init',
            '--recursive'
        ]
        subprocess.check_call(command, cwd=auto_build_path)

    shutil.copyfile('base.Dockerfile', os.path.join(workdir, 'base.Dockerfile'))
    shutil.copyfile('target.Dockerfile', os.path.join(workdir, 'target.Dockerfile'))
    shutil.copyfile('codeql.Dockerfile', os.path.join(workdir, 'codeql.Dockerfile'))
    shutil.copyfile('transform.py', os.path.join(workdir, 'transform.py'))
    shutil.copyfile('runner.py', os.path.join(workdir, 'runner.py'))
    shutil.copyfile('triage.py', os.path.join(workdir, 'triage.py'))


if __name__ == "__main__":
    with open("config.yml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            os.abort()

    print(config)

    if 'workdir' in config:
        workdir = config['workdir']
    else:
        workdir = os.getcwd()

    if not os.path.exists(workdir):
        os.mkdir(workdir)

    setup_environment(workdir)
    build_base_image(workdir)

    targets = []
    for target in ['current', 'earlier']:
        if target in config['target']:
            targets.append(config['target'][target])

    build_target_image(targets, workdir)
    build_codeql_image(targets, workdir)
