from src.ast2java.statements.Statement import Statement
from src.ast2java.statements.Block import Block


class UncheckedStatement(Statement):
    def __init__(self, _ast, parent, eol):
        super().__init__(_ast, parent, eol)

    def get_content(self):
        result = f"{self.eol}_unchecked_start();"
        result += f"{self.eol}"
        result += Block(self.ast.get('body'), self, self.eol).get_content()
        return result
