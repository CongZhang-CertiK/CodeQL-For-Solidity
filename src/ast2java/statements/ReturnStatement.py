from src.ast2java.statements.Statement import Statement
from src.ast2java.expressions.Expression import Expression


class ReturnStatement(Statement):
    def __init__(self, _ast, parent, eol):
        super().__init__(_ast, parent, eol)

    def get_content(self):
        result = f"{self.eol}return {Expression(self.ast.get('expression'), self).get_content()};"
        return result
