from src.ast2java.expressions.Expression import Expression


class UnaryOperation:
    def __init__(self, ast):
        self.ast = ast
        self.sub_expression = Expression(self.ast.get('subExpression'))
        self.operator = self.ast.get('operator')
        self.is_prefix = self.ast.get('isPrefix')

    def get_content(self):
        if self.is_prefix:
            return self.operator + self.sub_expression.get_content()
        else:
            return self.sub_expression.get_content() + self.operator
