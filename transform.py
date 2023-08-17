# Copyright 2023 CertiK
# This code is proprietary and not licensed. It is intended for internal use at CertiK only.
# Author: Ju Chen (ju.chen@certik.com)

# Runs ```paresol``` for each file in a directory (recursively).
# For now, we use symbol links to fix the missing links for solidity ```imports```
# Specifically, we create symbol links in each sub-directory of the target project. Those symbol links point to the
# library files downloaded by ```auto-build```.


import os
import subprocess
import shutil
import triage
import difflib


def contain_solidity_file(dir):
    '''Check if a directory contains any solidity file'''
    for directory in next(os.walk(dir))[1]:
        for root, subdirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".sol"):
                    return True
    return False


def create_symbol_link(src_dir, dst_dir, dir_list):
    for dir in dir_list:
        dst_subdir = os.path.join(dst_dir, dir)
        if not os.path.exists(dst_subdir):
            rel = os.path.relpath(src_dir, dst_dir)
            os.symlink(os.path.join(rel, dir), dst_subdir)


def get_dirs_with_solidity_files(src_dir):
    dir_list = []
    for dir in next(os.walk(src_dir))[1]:
        src_subdir = os.path.join(src_dir, dir)
        if contain_solidity_file(src_subdir):
            dir_list.append(dir)
    return dir_list


def fix_imports_by_symbol_links(dst_dir):
    src_dir = os.path.join(dst_dir, "node_modules")
    if not os.path.exists(src_dir):
        return
    dir_list = get_dirs_with_solidity_files(src_dir)
    create_symbol_link(os.path.join(
        dst_dir, "node_modules"), dst_dir, dir_list)
    #for root, subdirs, files in os.walk(dst_dir):
    #    symbol_link_created = False
    #    # skip node_modues
    #    if "node_modules" in root:
    #        continue
    #    for file in files:
    #        if file.endswith(".sol"):
    #            if not symbol_link_created:
    #                create_symbol_link(os.path.join(
    #                    dst_dir, "node_modules"), root, dir_list)
    #                symbol_link_created = True


def rewrite_file(tmp_file):
    """keep the content after @0. If there's no @0 in the file (new paresol version), this fucntion has no effect"""
    lines = []
    start = 0
    found_token = False
    with open(tmp_file, 'r') as outfile:
        lines = outfile.readlines()
        for line in lines:
            if line[0] == '@' and line[1] == '0':
                found_token = True
                break
            start = start + 1
        if not found_token:
            start = 0
        else:
            start = start + 1
    with open(tmp_file, 'w') as outfile:
        for i in range(start, len(lines)):
            outfile.write(lines[i])


def write_diff(diff_file_path, from_file, to_file):
    with open(from_file, 'r') as hosts0:
        with open(to_file, 'r') as hosts1:
            with open(diff_file_path, 'w') as outfile:
                diff = difflib.unified_diff(
                    hosts0.readlines(),
                    hosts1.readlines(),
                    fromfile=from_file,
                    tofile=to_file,
                )
                for line in diff:
                    outfile.write(line)


def handle_file(workdir, root, file, diff_file_path, flattened_file_path, project_name):
    src_file = os.path.join(root, file)
    stdout_file_name = str(file) + "_stdout"
    stderr_file_name = str(file) + "_stderr"
    stdout_file = os.path.join(root, stdout_file_name)
    stderr_file = os.path.join(root, stderr_file_name)
    return_code = 0
    with open(stdout_file, 'w') as outfile, open(stderr_file, 'w') as errfile:
        result = subprocess.run(["paresol", src_file],
                                cwd=workdir, stdout=outfile, stderr=errfile)
        return_code = result.returncode
        if return_code == 0:
            # transform success, let's keep the section after "@0"
            rewrite_file(stdout_file)
            write_diff(diff_file_path, src_file, stdout_file)
            shutil.copyfile(stdout_file, flattened_file_path)
    if return_code != 0:
        os.remove(flattened_file_path)
        error_written = False
        with open(stderr_file, 'r') as file:
            data = file.read()
            if len(data) != 0:
                triage.report_transform_error(
                    project_name, str(src_file), data)
                error_written = True
        if not error_written:
            with open(stdout_file, 'r') as file:
                data = file.read()
                if len(data) != 0:
                    triage.report_transform_error(
                        project_name, str(src_file), data)
    os.remove(stderr_file)
    os.remove(stdout_file)


def walk_files(input_dir, diff_dir, flattened_dir, project_name, output_dir, failed_set):
    fix_imports_by_symbol_links(input_dir)
    for root, subdirs, files in os.walk(input_dir):
        if "node_modules" in root:
            continue
        for file in files:
            # skip files that can't be built by auto-build
            if os.path.join(root, file) in failed_set:
                continue
            if file.endswith(".sol"):
                diff_file_path = os.path.join(
                    diff_dir, os.path.relpath(root, input_dir), file)
                flattened_file_path = os.path.join(
                    flattened_dir, os.path.relpath(root, input_dir), file)
                handle_file(input_dir, root, file, diff_file_path, flattened_file_path, project_name)
    triage.save_transform_errors(output_dir)