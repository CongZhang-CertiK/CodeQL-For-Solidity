from .JavaSourceFile import JavaSourceFile
from src.logger import logger
from src.config import CONFIG


def gen_java_from_ast(source_unit):
    move_builtins_to_dist()
    current_source_file = None
    for cu in source_unit.get('children'):
        if cu.get('type') == "PragmaDirective" and current_source_file is None:
            current_source_file = JavaSourceFile()
            current_source_file.pragma_info = f"// pragma {cu.get('name')} {cu.get('value')};"
            continue
        elif cu.get('type') == "ContractDefinition" and current_source_file is not None:
            current_source_file.compilation_unit = cu
            current_source_file.update(cu)
            current_source_file.write_to_file()
            current_source_file = None
        else:
            logger.debug("[Unexpected Control Flow]")
            logger.debug("Current Source File: ", current_source_file)
            logger.debug("Compilation Unit Type: ", cu.get('type'))


def move_builtins_to_dist():
    import shutil
    shutil.move(CONFIG.builtins, CONFIG.dist)
