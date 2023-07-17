from src.ast2java.keywordMapping import keyword_map, resolve_type


class Parameter:
    def __init__(self, ast):
        self.ast = ast
        assert self.ast.get('type') == "Parameter" or self.ast.get('type') == 'VariableDeclaration'
        self.type_type = self.ast.get('typeName').get('type')
        self.type_name = resolve_type(self.ast.get('typeName'))
        self.name = self.ast.get('name')
        self.storage_location = self.ast.get('storageLocation')
        self.is_state_var = self.ast.get('isStateVar')
        self.is_indexed = self.ast.get('isIndexed')

    def get_content(self):
        result = ""
        if self.storage_location is not None:
            result += f"@{keyword_map(self.storage_location)} "
        result += keyword_map(self.type_name)
        if self.name is not None:
            result += " " + self.name
        return result
