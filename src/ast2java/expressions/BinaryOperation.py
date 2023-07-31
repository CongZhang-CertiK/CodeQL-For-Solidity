from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map


class BinaryOperation:
    def __init__(self, ast):
        self.ast = ast
        self.left = Expression(self.ast.get('left'))
        self.right = Expression(self.ast.get('right'))
        self.operator = self.ast.get('operator')

    def get_content(self):
        evm_op = keyword_map(self.operator)
        if evm_op != self.operator:
            return f"{keyword_map(self.operator)}({self.left.get_content()}, {self.right.get_content()})"
        else:
            return f"{self.left.get_content()} {self.operator} {self.right.get_content()}"