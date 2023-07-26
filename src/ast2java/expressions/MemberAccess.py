from src.ast2java.expressions.Expression import Expression


class MemberAccess:
    def __init__(self, ast):
        self.ast = ast
        self.expression = Expression(self.ast.get('expression'))
        self.member_name = self.ast.get('memberName')

    def get_content(self):
        return self.expression.get_content() + '.' + self.member_name