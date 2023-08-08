from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map
from .BaseExpression import BaseExpression


class NumberLiteral(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.num = self.ast.get('number')
        self.value = self.convert_to_decimal()

    def convert_to_decimal(self):
        if self.num.startswith('0x'):
            return int(self.num, 16)
        else:
            return int(self.num, 10)

    def get_content(self):
        if self.value > 2147483647:
            result = f"_uint({self.num}L)"
        else:
            result = f"_uint({self.num})"
        return result
