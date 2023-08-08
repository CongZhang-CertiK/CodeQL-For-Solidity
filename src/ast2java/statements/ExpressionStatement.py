from src.ast2java.statements.Statement import Statement
from src.ast2java.expressions.Expression import Expression


class ExpressionStatement(Statement):
    def __init__(self, _ast, parent, eol):
        super().__init__(_ast, parent, eol)
        self.expression = Expression(self.ast.get('expression'), self)

    def get_content(self):
        result = self.eol
        result += self.expression.get_content()
        result += ";"
        return result
