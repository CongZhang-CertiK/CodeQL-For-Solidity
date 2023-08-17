import os
import subprocess
import concurrent.futures
import yaml
import shutil


def run_docker(project_id, ocaml_solidity_version, paresol_version, codeql_version, workdir):
    """Start end-to-end testing by running a script inside a runner image's Docker container"""
    container_name = f'codeql_runner_for_{project_id.lower()}_{ocaml_solidity_version}_{paresol_version}'
    workdir_real = os.path.realpath(workdir)
    output_dir_host = os.path.join(
        workdir_real, f'output_{ocaml_solidity_version}_{paresol_version}', f'{project_id}')
    if os.path.exists(output_dir_host):
        shutil.rmtree(output_dir_host)
    input_dir_host = os.path.join(workdir_real, 'input', f'{project_id}')
    environment_args = [
        '-e',
        'INPUT_TRANSFORMED=/workdir/projects-copy',
        '-e',
        'INPUT=/workdir/projects',
        '-e',
        'INPUT_DIFF=/workdir/projects-diff',
        '-e',
        f'PROJECT_ID={project_id}',
        '-e',
        'OUTPUT_DIR=/workdir/output'
    ]
    command = [
        'docker',
        'run',
        '-ti',
        '--rm',
        '--platform',
        'linux/x86_64',
        '-v',
        f'{output_dir_host}:/workdir/output',
        '-v',
        f'{input_dir_host}:/workdir/input',
    ] + environment_args + [
        f'--name={container_name}',
        f'codeql_build_{ocaml_solidity_version}_{paresol_version}_{codeql_version}',
        # '/bin/bash'
        'python3',
        'runner.py'
    ]
    return subprocess.check_call(command, cwd=workdir)


def setup_projects(projects, workdir):
    """copy projects to the destination"""
    if not os.path.exists(os.path.join(workdir, 'input')):
        os.mkdir(os.path.join(workdir, 'input'))
    for project in projects:
        project_id = project['project']['id']
        project_dir = os.path.join(workdir, 'input', project_id)
        if 'loc' in project['project']:
            if not os.path.exists(project_dir):
                shutil.copytree(os.path.join(workdir, project['project']['loc']), project_dir)


def run_targets(targets, config, workdir):
    """Submit runners to the threadpool. Each runner does end-to-end testing on a project"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for target in targets:
            ocaml_solidity_version = target['ocaml_solidity_version']
            paresol_version = target['paresol_version']
            codeql_version = target['codeql_version']
            for project in config['projects']:
                futures.append(
                    executor.submit(
                        run_docker,
                        project['project']['id'],
                        ocaml_solidity_version, paresol_version, codeql_version, workdir
                    )
                )
        for future in concurrent.futures.as_completed(futures):
            try:
                print(future.result())
            except Exception:
                pass


if __name__ == "__main__":
    with open("config.yml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            os.abort()

    workdir = config['workdir']

    targets = []
    for target in ['current', 'earlier']:
        if target in config['target']:
            targets.append(config['target'][target])

    setup_projects(config['projects'], workdir)

    run_targets(targets, config, workdir)

