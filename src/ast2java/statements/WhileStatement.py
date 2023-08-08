from src.ast2java.statements.Statement import Statement
from src.ast2java.statements.Block import Block
from src.ast2java.expressions.Expression import Expression


class WhileStatement(Statement):
    def __init__(self, _ast, parent, eol):
        super().__init__(_ast, parent, eol)

    def get_content(self):
        result = f"{self.eol}while ({Expression(self.ast.get('condition'), self).get_content()})"
        result += Block(self.ast.get('body'), self, self.eol).get_content()
        return result
