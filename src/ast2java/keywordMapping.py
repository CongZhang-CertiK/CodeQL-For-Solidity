from src.logger import logger

keyword_dict = {
    # "address": "Address",
    # "calldata": "Calldata",
    # "memory": "Memory",
    # "storage": "Storage",
    "string": "String",
    # "external": "External",
    # "internal": "Internal",
    "public": "_public",
    "private": "_private",
    # "view": "View",
    # "pure": "Pure",
    "bool": "Boolean",
    "True": "true",
    "False": "false",
    # "bytes": "Bytes",
    # "bytes1": "Bytes1",
    # "bytes2": "Bytes2",
    # "bytes3": "Bytes3",
    # "bytes4": "Bytes4",
    # "bytes5": "Bytes5",
    # "bytes6": "Bytes6",
    # "bytes7": "Bytes7",
    # "bytes8": "Bytes8",
    # "bytes9": "Bytes9",
    # "bytes10": "Bytes10",
    # "bytes11": "Bytes11",
    # "bytes12": "Bytes12",
    # "bytes13": "Bytes13",
    # "bytes14": "Bytes14",
    # "bytes15": "Bytes15",
    # "bytes16": "Bytes16",
    # "bytes17": "Bytes17",
    # "bytes18": "Bytes18",
    # "bytes19": "Bytes19",
    # "bytes20": "Bytes20",
    # "bytes21": "Bytes21",
    # "bytes22": "Bytes22",
    # "bytes23": "Bytes23",
    # "bytes24": "Bytes24",
    # "bytes25": "Bytes25",
    # "bytes26": "Bytes26",
    # "bytes27": "Bytes27",
    # "bytes28": "Bytes28",
    # "bytes29": "Bytes29",
    # "bytes30": "Bytes30",
    # "bytes31": "Bytes31",
    # "bytes32": "Bytes32",
    # "uint8": "UInt8",
    # "uint16": "UInt16",
    # "uint24": "UInt24",
    # "uint32": "UInt32",
    # "uint40": "UInt40",
    # "uint48": "UInt48",
    # "uint56": "UInt56",
    # "uint64": "UInt64",
    # "uint72": "UInt72",
    # "uint80": "UInt80",
    # "uint88": "UInt88",
    # "uint96": "UInt96",
    # "uint104": "UInt104",
    # "uint112": "UInt112",
    # "uint120": "UInt120",
    # "uint128": "UInt128",
    # "uint136": "UInt136",
    # "uint144": "UInt144",
    # "uint152": "UInt152",
    # "uint160": "UInt160",
    # "uint168": "UInt168",
    # "uint176": "UInt176",
    # "uint184": "UInt184",
    # "uint192": "UInt192",
    # "uint200": "UInt200",
    # "uint208": "UInt208",
    # "uint216": "UInt216",
    # "uint224": "UInt224",
    # "uint232": "UInt232",
    # "uint240": "UInt240",
    # "uint248": "UInt248",
    # "uint256": "UInt256",
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
