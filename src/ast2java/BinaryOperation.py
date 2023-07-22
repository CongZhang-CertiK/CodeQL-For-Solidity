from .Expression import Expression


class BinaryOperation:
    def __init__(self, ast):
        self.ast = ast
        self.left = Expression(self.ast.get('left'))
        self.right = Expression(self.ast.get('right'))
        self.operator = self.ast.get('operator')

    def get_content(self):
        return self.left.get_content() + f" {self.operator} " + self.right.get_content()