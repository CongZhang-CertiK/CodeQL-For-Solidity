from src.ast2java.statements.Statement import Statement
from src.ast2java.expressions.Expression import Expression


class EmitStatement(Statement):
    def __init__(self, _ast, eol):
        super().__init__(_ast, eol)

    def get_content(self):
        result = f"{self.eol}{Expression(self.ast.get('eventCall')).get_content()};"
        return result
