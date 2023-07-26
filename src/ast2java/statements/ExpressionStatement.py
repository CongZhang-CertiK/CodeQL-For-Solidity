from src.ast2java.statements.Statement import Statement
from src.ast2java.expressions.Expression import Expression


class ExpressionStatement(Statement):
    def __init__(self, ast, eol):
        super().__init__(ast, eol)
        self.expression = Expression(self.ast.get('expression'))

    def get_content(self):
        result = self.eol
        result += self.expression.get_content()
        result += ";"
        return result
