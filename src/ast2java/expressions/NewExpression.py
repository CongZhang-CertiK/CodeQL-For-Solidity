from src.ast2java.expressions.Expression import Expression
from .BaseExpression import BaseExpression


class NewExpression(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.type_name = Expression(self.ast.get('typeName'), self)

    def get_content(self):
        return f"new {self.type_name.get_content()}"
