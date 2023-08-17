# Copyright 2023 CertiK
# This code is proprietary and not licensed. It is intended for internal use at CertiK only.
# Author: Ju Chen (ju.chen@certik.com)

# Issue triage and automatic reporting (in-development)

import json
import os

triage_data = []


def report_transform_error(project_name, file_name, raw_content):
    """Called by paresol during flattening"""
    record = {"project": project_name,
              "file": file_name,
              "content": raw_content}
    triage_data.append(record)


def save_transform_errors(output_dir):
    """save errors in flattening"""
    output_file_path = os.path.join(output_dir, 'report.json')
    with open(output_file_path, 'w') as final:
        json.dump(triage_data, final, indent=4)

# walk through all report in a output directory


def walk_file(input_file, aggregate_errors):
    with open(input_file, 'r') as input:
        data = json.load(input)
        for item in data:
            lines = item['content'].splitlines()
            location = ''
            error = ''
            if len(lines) < 3:
                # paresol does not report error here
                location = item['file']
                error = 'Paresol fails to report error type'
            else:
                for line in lines:
                    if 'Syntax error' in line or 'Type error' in line:
                        error = line.strip()
                    if '[ERROR] Aborting' in line:
                        location = line.strip()
            record = {"error": error,
                      "location": location}
            aggregate_errors.append(record)


def deduplicate_paresol_errors(aggregate_errors):
    """basic error deduplication based on error and location"""
    location_set = set()
    error_set = set()
    reduced_errors = []
    for error in aggregate_errors:
        if error['error'] == 'Paresol fails to report error type':
            reduced_errors.append(error)
        else:
            if error['location'] in location_set or error['error'] in error_set:
                continue
            else:
                location_set.add(error['location'])
                error_set.add(error['error'])
                reduced_errors.append(error)
    return reduced_errors


def walk_all_paresol_reports(output_dir):
    """aggreate all errors in a run"""
    aggregate_errors = []
    for root, subdirs, files in os.walk(output_dir):
        for file in files:
            if file == 'report.json':
                walk_file(os.path.join(root, file), aggregate_errors)
    deduplicated_errors = deduplicate_paresol_errors(aggregate_errors)
    return deduplicated_errors


def compare_build_status(ori_records, trans_records):
    """Compare the build status (fail/OK) between original files and flattened files"""
    ok_set = set()
    fail_set = set()
    for record in ori_records:
        file = record.split(':')[0]
        status = record.split(':')[1][1:-1]
        if status == 'OK':
            ok_set.add(file)
        else:
            fail_set.add(file)
    err_set = set()
    for record in trans_records:
        file = record.split(':')[0]
        status = record.split(':')[1][1:-1]
        if status == 'Fail' and file in ok_set:
            err_set.add(file)
    return err_set


def extract_build_errors(err_set, build_error):
    """Extract build errors from """
    records = []
    record = {}
    record_start = False
    for line in build_error:
        if 'compile_error' in line:
            if record_start:
                records.append(record.copy())
        elif 'contract dir' in line:
            file = line.split(':')[1][1:-1]
            if file in err_set:
                record['file'] = file
                record['content'] = []
                record_start = True
        elif 'missing_source' in line:
            continue
        else:
            if record_start:
                record['content'].append(line.strip())
    if record_start:
        records.append(record)
    return records


def walk_all_auto_build_reports(output_dir):
    """Check if a flattened file can't be compiled (but original file can). If so, extract the build errors and report"""
    records = []
    for project in os.listdir(output_dir):
        ori_status_file = os.path.join(
            output_dir, project, 'auto_build_artifacts_original', 'target-status.txt')
        trans_status_file = os.path.join(
            output_dir, project, 'auto_build_artifacts_transformed', 'target-status.txt')
        build_error_file = os.path.join(
            output_dir, project, 'auto_build_artifacts_transformed', 'build-errors.txt')
        err_set = set()
        # compare target status from original project and flattened project,
        # save the list of the problematic flattened files
        if os.path.exists(ori_status_file) and os.path.exists(trans_status_file):
            with open(ori_status_file) as ori_status, open(trans_status_file) as trans_status:
                err_set = compare_build_status(ori_status, trans_status)
        # extract the build errors for those problematic flattened files and report
        if os.path.exists(build_error_file):
            with open(build_error_file) as build_error:
                records += extract_build_errors(err_set, build_error)
    return records


def save_report(data, output_file_path):
    """save report"""
    with open(output_file_path, 'w') as final:
        json.dump(data, final, indent=4)


def regression_check(earlier, later, workdir):
    output_earlier = os.path.join(workdir, 'output' + '_' + \
        earlier['ocaml_solidity_version'] + '_' + earlier['paresol_version'])
    output_later = os.path.join(workdir, 'output' + '_' + \
        later['ocaml_solidity_version'] + '_' + later['paresol_version'])

    # check if there is any regression on compiling flattened files
    records_earlier = walk_all_auto_build_reports(output_earlier)
    records_later = walk_all_auto_build_reports(output_later)
    files_set_earlier = set()
    compile_regression_record = []
    for record in records_earlier:
        files_set_earlier.add(record['file'])
    for record in records_later:
        if record['file'] not in files_set_earlier:
            compile_regression_record.append(record)
    save_report(compile_regression_record, os.path.join(workdir, 'regression_compilation.json'))

    # check if there is any regression on flattening
    transform_regression_record = []
    records_earlier = walk_all_paresol_reports(output_earlier)
    records_later = walk_all_paresol_reports(output_later)
    error_set_earlier = set()
    for record in records_earlier:
        error_set_earlier.add(record['error'])
    for record in records_later:
        if record['error'] not in error_set_earlier:
            transform_regression_record.append(record)
    save_report(transform_regression_record, os.path.join(workdir, 'regression_transform.json'))


def transform_error_report(version, workdir):
    output_dir = os.path.join(workdir, 'output' + '_' + \
        version['ocaml_solidity_version'] + '_' + version['paresol_version'])
    records = walk_all_paresol_reports(output_dir)
    save_report(records, os.path.join(workdir, 'transform_errors.json'))


def compilation_error_report(version, workdir):
    output_dir = os.path.join(workdir, 'output' + '_' + \
        version['ocaml_solidity_version'] + '_' + version['paresol_version'])
    records = walk_all_auto_build_reports(output_dir)
    save_report(records, os.path.join(workdir, 'compilation_errors.json'))


if __name__ == "__main__":
    """Unit tests"""
    version_earlier = {
        'ocaml_solidity_version': 'v0.5.6-visitors', 'paresol_version': '0.0.3'}
    version_later = {
        'ocaml_solidity_version': 'v0.5.9-visitors', 'paresol_version': '0.0.5'}
    regression_check(version_earlier, version_later)