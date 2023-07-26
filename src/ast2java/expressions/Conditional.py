from src.ast2java.expressions.Expression import Expression


class Conditional:
    def __init__(self, ast):
        self.ast = ast
        self.condition = Expression(self.ast.get('condition'))
        self.true_expression = Expression(self.ast.get('TrueExpression'))
        self.false_expression = Expression(self.ast.get('FalseExpression'))

    def get_content(self):
        return f"{self.condition.get_content()} ? " \
               f"{self.true_expression.get_content()} : {self.false_expression.get_content()}"
