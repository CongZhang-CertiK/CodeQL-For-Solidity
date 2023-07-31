from src.logger import logger

keyword_dict = {
    # keyword
    "public": "_public",
    "private": "_private",
    # function
    "revert": "_revert",
    "require": "_require",
    # type
    "string": "String",
    "bool": "Boolean",
    # expression
    "True": "true",
    "False": "false",
    # operator
    "+": "_add",
    "-": "_sub",
    "/": "_div",
    "//": "_mod",
    "*": "_mul",
    "**": "_pow",
    "==": "_equal",
    "!=": "_notEqual",
    ">": "_greaterThan",
    "<": "_lessThan",
    ">=": "_greaterEqual",
    "<=": "_lessEqual",
    "=": "_assign",
    "+=": "_addAssign",
    "-=": "_subAssign",
    "*=": "_mulAssign",
    "/=": "_divAssign",
    "//=": "_modAssign",
    ">>": "_rightShift",
    "<<": "_leftShift",
    ">>=": "_rightShiftAssign",
    "<<=": "_leftShiftAssign"
}


def keyword_map(type_name):
    if type_name is None:
        return "NoneType"
    return keyword_dict.get(type_name, type_name)


def resolve_type(ast):
    node_type = ast.get('type')
    if node_type == "ElementaryTypeName":
        return keyword_map(ast.get('name'))
    elif node_type == "UserDefinedTypeName":
        return ast.get('namePath')
    elif node_type == "Mapping":
        key = resolve_type(ast.get('keyType'))
        value = resolve_type(ast.get('valueType'))
        return f"Map<{key}, {value}>"
    elif node_type == "ArrayTypeName":
        base_type = resolve_type(ast.get('baseTypeName'))
        return f"ArrayList<{base_type}>"
    else:
        logger.debug("unresolved type" + node_type)
        return "None"


# def resolve_type(ast):
#     node_type = ast.get('type')
#     if node_type == "ElementaryTypeName" or node_type == "UserDefinedTypeName":
#         return _resolve_type(ast)
#     elif node_type == "Mapping":
#         return f"Map{_resolve_type(ast)}"
#     else:
#         logger.debug("unresolved type" + node_type)
#         return "None"
