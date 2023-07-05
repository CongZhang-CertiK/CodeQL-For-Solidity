from src.ast2java.keywordMapping import keyword_map


class Parameter:
    def __init__(self, ast):
        self.ast = ast
        assert self.ast.get('type') == "Parameter"
        self.type_type = self.ast.get('typeName').get('type')
        self.type_name = self.ast.get('typeName').get('name')
        self.name = self.ast.get('name')

    def get_content(self):
        result = ""
        result += keyword_map(self.type_name)
        result += " "
        if self.name is None:
            result += "NONE_PARAM"
        else:
            result += self.name
        return result
