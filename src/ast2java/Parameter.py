from src.ast2java.typeMap import type_map

class Parameter:
    def __init__(self, compilation_unit):
        self.cu = compilation_unit
        assert self.cu.get('type') == "Parameter"
        self.type_type = self.cu.get('typeName').get('type')
        self.type_name = self.cu.get('typeName').get('name')
        self.name = self.cu.get('name')

    def get_content(self):
        result = ""
        if self.type_name is None:
            result += "NONE_TYPE"
        elif self.type_name in type_map.bytes:
            result += self.type_name.replace("bytes", "Bytes")
        elif self.type_name in type_map.uint:
            result += self.type_name.replace("uint", "UInt")
        elif self.type_name == "address":
            result += "Address"
        elif self.type_name == "string":
            result += "String"
        else:
            result += self.type_name
        result += " "
        if self.name is None:
            result += "NONE_PARAM"
        else:
            result += self.name
        return result
