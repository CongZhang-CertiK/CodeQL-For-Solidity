from src.ast2java.keywordMapping import keyword_map


class Parameter:
    def __init__(self, ast):
        self.ast = ast
        assert self.ast.get('type') == "Parameter"
        self.type_type = self.ast.get('typeName').get('type')
        if self.type_type == "ElementaryTypeName":
            self.type_name = self.ast.get('typeName').get('name')
        elif self.type_type == "UserDefinedTypeName":
            self.type_name = self.ast.get('typeName').get('namePath')
        else:
            self.type_name = None
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
