from src.ast2java.statements.Statement import Statement
from src.ast2java.expressions.Expression import Expression


class ReturnStatement(Statement):
    def __init__(self, _ast, parent, eol):
        super().__init__(_ast, parent, eol)
        self.return_expression = Expression(self.ast.get('expression'), self)
        self.function = self.return_expression.find_function()
        if self.function is not None:
            self.return_type = self.function.return_type
        else:
            self.return_type = None

    def get_content(self):
        from src.ast2java.keywordMapping import keyword_map, function_dict
        if self.return_type is not None and self.return_type in function_dict.keys():
            type_cast = keyword_map(self.return_type, function=True)
            result = f"{self.eol}return {type_cast}({self.return_expression.get_content()});"
        else:
            result = f"{self.eol}return {self.return_expression.get_content()};"
        return result
