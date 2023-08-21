from src.logger import logger

keyword_dict = {
    # keyword
    "public": "_public",
    "private": "_private",
    # type
    # "string": "String",
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
    # "=": "_assign",
    "+=": "_addAssign",
    "-=": "_subAssign",
    "*=": "_mulAssign",
    "/=": "_divAssign",
    "//=": "_modAssign",
    ">>": "_rightShift",
    "<<": "_leftShift",
    ">>=": "_rightShiftAssign",
    "<<=": "_leftShiftAssign",
    "&": "_and",
    "|": "_or",
    "^": "_xor",
    "~": "_not",
    "++": "_increment",
    "--": "_decrement",
    "&=": "_andAssign",
    "|=": "_orAssign",
    "^=": "_xorAssign"
}

function_dict = {
    "revert": "_revert",
    "require": "_require",
    "keccak256": "_keccak256",
    "ecrecover": "_ecrecover",
    "string": "_string",
    "address": "_address",
    "Boolean": "_Boolean",
    "type": "_type",
    "uint8": "_uint8",
    "uint16": "_uint16",
    "uint24": "_uint24",
    "uint32": "_uint32",
    "uint40": "_uint40",
    "uint48": "_uint48",
    "uint56": "_uint56",
    "uint64": "_uint64",
    "uint72": "_uint72",
    "uint80": "_uint80",
    "uint88": "_uint88",
    "uint96": "_uint96",
    "uint104": "_uint104",
    "uint112": "_uint112",
    "uint120": "_uint120",
    "uint128": "_uint128",
    "uint136": "_uint136",
    "uint144": "_uint144",
    "uint152": "_uint152",
    "uint160": "_uint160",
    "uint168": "_uint168",
    "uint176": "_uint176",
    "uint184": "_uint184",
    "uint192": "_uint192",
    "uint200": "_uint200",
    "uint208": "_uint208",
    "uint216": "_uint216",
    "uint224": "_uint224",
    "uint232": "_uint232",
    "uint240": "_uint240",
    "uint248": "_uint248",
    "uint256": "_uint256",
    "bytes": "_bytes",
    "bytes1": "_bytes1",
    "bytes2": "_bytes2",
    "bytes3": "_bytes3",
    "bytes4": "_bytes4",
    "bytes5": "_bytes5",
    "bytes6": "_bytes6",
    "bytes7": "_bytes7",
    "bytes8": "_bytes8",
    "bytes9": "_bytes9",
    "bytes10": "_bytes10",
    "bytes11": "_bytes11",
    "bytes12": "_bytes12",
    "bytes13": "_bytes13",
    "bytes14": "_bytes14",
    "bytes15": "_bytes15",
    "bytes16": "_bytes16",
    "bytes17": "_bytes17",
    "bytes18": "_bytes18",
    "bytes19": "_bytes19",
    "bytes20": "_bytes20",
    "bytes21": "_bytes21",
    "bytes22": "_bytes22",
    "bytes23": "_bytes23",
    "bytes24": "_bytes24",
    "bytes25": "_bytes25",
    "bytes26": "_bytes26",
    "bytes27": "_bytes27",
    "bytes28": "_bytes28",
    "bytes29": "_bytes29",
    "bytes30": "_bytes30",
    "bytes31": "_bytes31",
    "bytes32": "_bytes32"
}


def keyword_map(type_name, function=False):
    if type_name is None:
        return "NoneType"
    if not function:
        return keyword_dict.get(type_name, type_name)
    else:
        return function_dict.get(type_name, type_name)


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
        return f"array<{base_type}>"
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
