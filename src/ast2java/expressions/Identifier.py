from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map
from .BaseExpression import BaseExpression


class Identifier(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.name = self.ast.get('name')
        self.contract = self.find_contract()

    def get_content(self):
        result = self.name
        return result

    def get_exp_type(self):
        return "uint8"
