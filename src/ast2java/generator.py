from .JavaSourceFile import JavaSourceFile
from src.logger import logger
from src.config import CONFIG


def gen_java_from_ast(source_unit):
    copy_builtins_to_dist()
    current_source_file = None
    for ast in source_unit.get('children'):
        if ast.get('type') == "PragmaDirective" and current_source_file is None:
            current_source_file = JavaSourceFile()
            current_source_file.pragma_info = f"// pragma {ast.get('name')} {ast.get('value')};"
            continue
        elif ast.get('type') == "ContractDefinition" and current_source_file is not None:
            current_source_file.ast = ast
            current_source_file.update(ast)
            current_source_file.write_to_file()
            current_source_file = None
        else:
            logger.debug("[Unexpected Control Flow]")
            logger.debug("Current Source File: ", current_source_file)
            logger.debug("AST Node Type: ", ast.get('type'))


def copy_builtins_to_dist():
    import shutil
    import os
    builtin_dist = CONFIG.dist + "/builtins"
    if os.path.exists(builtin_dist):
        shutil.rmtree(builtin_dist)
    shutil.copytree(CONFIG.builtins, builtin_dist)
