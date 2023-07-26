from src.ast2java.definitions.JavaSourceFile import JavaSourceFile
from src.logger import logger
from src.config import CONFIG
from .compilationGlobal import compilation_global


def gen_java_from_ast(source_unit):
    copy_builtins_to_dist()
    compilation_units_list = scatter_to_compilation_units(source_unit)
    for compilation_unit in compilation_units_list:
        pragma_directive, contract_definition = compilation_unit
        current_source_file = JavaSourceFile(compilation_global)
        current_source_file.pragma_info = f"// pragma {pragma_directive.get('name')} {pragma_directive.get('value')};"
        current_source_file.ast = contract_definition
        current_source_file.update(contract_definition)
        compilation_global[contract_definition.name] = current_source_file
        current_source_file.write_to_file()


def scatter_to_compilation_units(source_unit):
    compilation_units = {}
    pragma_directive = None
    for ast in source_unit.get('children'):
        if ast.get('type') == "PragmaDirective" and pragma_directive is None:
            pragma_directive = ast
        elif ast.get('type') == "ContractDefinition" and pragma_directive is not None:
            compilation_units[ast.get('name')] = (pragma_directive, ast)
            pragma_directive = None
        else:
            logger.debug("unknown source unit children type.")
    return reorg_compilation_tree(compilation_units)


def reorg_compilation_tree(compilation_units_dict):
    reorged_list = []
    reorged_units = []
    while len(reorged_list) != len(compilation_units_dict.values()):
        for compilation_unit in compilation_units_dict.values():
            contract_definition = compilation_unit[1]
            name = contract_definition.get('name')
            if name in reorged_list:
                continue
            base_contracts = contract_definition.get('baseContracts')
            for base_contract in base_contracts:
                if base_contract.get('baseName').get('namePath') not in reorged_list:
                    continue
            reorged_list.append(name)
            reorged_units.append(compilation_unit)
    return reorged_units


def copy_builtins_to_dist():
    import shutil
    import os
    builtin_dist = CONFIG.dist + "/builtins"
    if os.path.exists(builtin_dist):
        shutil.rmtree(builtin_dist)
    shutil.copytree(CONFIG.builtins, builtin_dist)
