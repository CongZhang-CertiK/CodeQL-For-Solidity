from src.ast2java.expressions.Expression import Expression
from .BaseExpression import BaseExpression


class Conditional(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.condition = Expression(self.ast.get('condition'), self)
        self.true_expression = Expression(self.ast.get('TrueExpression'), self)
        self.false_expression = Expression(self.ast.get('FalseExpression'), self)

    def get_content(self):
        return f"{self.condition.get_content()} ? " \
               f"{self.true_expression.get_content()} : {self.false_expression.get_content()}"
