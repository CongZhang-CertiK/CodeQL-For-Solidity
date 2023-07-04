from src.sol2ast import parse_file_to_ast
from src.ast2java import gen_java_from_ast
from src.config import CONFIG
from src.logger import logger


def test_sol2ast():
    file_path = CONFIG.test_source
    source_unit = parse_file_to_ast(file_path)
    return source_unit


def test_ast2java(source_unit):
    gen_java_from_ast(source_unit)


def test():
    logger.debug("testing transformer")
    test_ast2java(test_sol2ast())


test()
