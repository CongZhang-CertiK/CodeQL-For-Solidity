from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map
from .BaseExpression import BaseExpression


class StringLiteral(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.value = self.ast.get('value').replace("\\", "\\\\")

    def get_content(self):
        return '"' + self.value + '"'

    def get_exp_type(self):
        return "string"
