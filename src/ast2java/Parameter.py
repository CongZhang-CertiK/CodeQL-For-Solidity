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
        else:
            result += self.type_name
        result += " "
        if self.name is None:
            result += "NONE_PARAM"
        else:
            result += self.name
        return result
