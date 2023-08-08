from src.ast2java.expressions.Expression import Expression
from .BaseExpression import BaseExpression


class MemberAccess(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.expression = Expression(self.ast.get('expression'), self)
        self.member_name = self.ast.get('memberName')

    def get_content(self):
        return self.expression.get_content() + '.' + self.member_name