import os.path

from src.sol2ast import parser
from src.logger import logger


def parse_file_to_ast(file_path: str):
    """
    parse solidity file to ast
    :param file_path: absolute path of solidity file
    :return: abstract syntax tree object
    """
    if not os.path.exists(file_path):
        logger.debug("File does not exists:", file_path)
        return None
    source_unit = parser.parse_file(file_path, loc=False)
    # loc=True -> add location information to ast nodes
    return source_unit

