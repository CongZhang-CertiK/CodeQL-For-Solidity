from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map
from .BaseExpression import BaseExpression


class ArrayTypeName(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.length = self.ast.get('length')
        self.baseType = Expression(self.ast.get('baseTypeName'), self)

    def get_content(self):
        if self.length is not None:
            return f"array<{self.baseType.get_content()}>({self.length})"
        else:
            return f"array<{self.baseType.get_content()}>"
