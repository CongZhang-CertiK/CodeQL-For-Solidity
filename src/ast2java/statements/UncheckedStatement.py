from src.ast2java.statements.Statement import Statement
from src.ast2java.statements.Block import Block


class UncheckedStatement(Statement):
    def __init__(self, _ast, eol):
        super().__init__(_ast, eol)

    def get_content(self):
        result = f"{self.eol}Boolean unchecked = true;"
        result += f"{self.eol}if(unchecked) "
        result += Block(self.ast.get('body'), self.eol).get_content()
        return result
