from src.ast2java.expressions.Expression import Expression

from src.ast2java.keywordMapping import keyword_map

class UnaryOperation:
    def __init__(self, ast):
        self.ast = ast
        self.sub_expression = Expression(self.ast.get('subExpression'))
        self.operator = self.ast.get('operator')
        self.is_prefix = self.ast.get('isPrefix')

    def get_content(self):
        evm_op = keyword_map(self.operator)
        if evm_op != self.operator:
            return f"{evm_op}({self.sub_expression.get_content()})"
        else:
            if self.is_prefix:
                return self.operator + self.sub_expression.get_content()
            else:
                return self.sub_expression.get_content() + self.operator
