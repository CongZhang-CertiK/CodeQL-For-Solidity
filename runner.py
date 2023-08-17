#!/usr/bin/env python3
# Copyright 2023 CertiK
# This code is proprietary and not licensed. It is intended for internal use at CertiK only.
# Author: Ju Chen (ju.chen@certik.com)
#
# The runner that executes end-to-end testing for a project
# 1. Run auto-build on the project.
# 2. Run ```paresol```` to transform each solidity file.
# 3. Run auto-build again on the transformed project.
# This python script is running inside a runner's container.


import transform
import os
import subprocess
import shutil


def cleanup(target_dir):
    """Remove non-solidity files to minimize the size of attachment for Github issue reporting"""
    for root, subdirs, files in os.walk(target_dir):
        for file in files:
            if not file.endswith(".sol"):
                src_file = os.path.join(root, file)
                os.remove(src_file)


input = os.getenv('INPUT', None)
input_transformed = os.getenv('INPUT_TRANSFORMED', None)
input_diff = os.getenv('INPUT_DIFF', None)
project_id = os.getenv('PROJECT_ID', None)
output_dir = os.getenv('OUTPUT_DIR', None)

my_env = os.environ.copy()
my_env["SINGLE_FILE_MODE_ONLY"] = '1'
my_env["PATH"] = "/workdir/auto-build/env/bin:" + my_env["PATH"]

shutil.copytree('/workdir/input', input)
shutil.copytree('/workdir/input', input_transformed)
shutil.copytree('/workdir/input', input_diff)

# run auto-build
auto_build_work_dir = os.path.join(output_dir, 'auto_build_artifacts_original')
os.mkdir(auto_build_work_dir)
result = subprocess.run(["/workdir/auto-build/auto-build.sh", input], env=my_env,
                        cwd=auto_build_work_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
return_code = result.returncode

# note which files can't be built
failed_set = set()
target_status_path = os.path.join(auto_build_work_dir, 'target-status.txt')
if os.path.exists(target_status_path):
    with open(target_status_path, 'r') as target_status:
        lines = target_status.readlines()
        for line in lines:
            status = line.strip()[-2:]
            if status != 'OK':
                failed_set.add(os.path.join(
                    input, line.split(':')[0]))

# copy node_modules
if os.path.exists(os.path.join(input, 'node_modules')):
    shutil.rmtree(os.path.join(input, 'node_modules'))
    shutil.copytree('/workdir/npm_modules/lib/node_modules', os.path.join(input, 'node_modules'))
    cleanup(os.path.join(input, 'node_modules'))

# save un-flattened source to a zip
shutil.make_archive(os.path.join(output_dir, 'orig'), 'tar', input)

if return_code == 0:
    print(f'Successfully built original {project_id}!')
    transform.walk_files(input, input_diff, input_transformed,
                         project_id, output_dir, failed_set)
else:
    print("Auto build failed on original project")

print(f'finished flattening {project_id}!')
shutil.make_archive(os.path.join(output_dir, 'tran'), 'tar', input_transformed)
shutil.make_archive(os.path.join(output_dir, 'diff'), 'tar', input_diff)
print(f'finished creating arfifacts {project_id}!')

# run auto-build on transformed project
auto_build_work_dir = os.path.join(
    output_dir, 'auto_build_artifacts_transformed')
os.mkdir(auto_build_work_dir)
result = subprocess.run(["/workdir/auto-build/auto-build.sh", input_transformed], env=my_env,
                        cwd=auto_build_work_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
return_code = result.returncode
# FIXME: partial success is a success?
if return_code == 0:
    print('Successfully built transformed project!')
else:
    print('Failed building transformed project!')