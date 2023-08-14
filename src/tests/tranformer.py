from src.sol2ast import parse_file_to_ast
from src.ast2java import gen_java_from_ast
from src.config import CONFIG
from src.logger import logger


def test_sol2ast():
    file_path = CONFIG.source
    source_unit = parse_file_to_ast(file_path)
    return source_unit


def test_ast2java(source_unit):
    import shutil
    import os
    builtin_dist = CONFIG.dist
    if os.path.exists(builtin_dist):
        shutil.rmtree(builtin_dist)
    os.mkdir(CONFIG.dist)
    builtin_dist = CONFIG.dist + "/builtins"
    # os.mkdir(builtin_dist)
    shutil.copytree(CONFIG.builtins, builtin_dist)
    gen_java_from_ast(source_unit)


def test():
    logger.debug("testing transformer")
    test_ast2java(test_sol2ast())


test()
