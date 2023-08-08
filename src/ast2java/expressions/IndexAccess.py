from src.ast2java.expressions.Expression import Expression
from .BaseExpression import BaseExpression


class IndexAccess(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.base = Expression(self.ast.get('base'), self)
        self.index = Expression(self.ast.get('index'), self)

    def get_content(self):
        return f"{self.base.get_content()}.get({self.index.get_content()})"
