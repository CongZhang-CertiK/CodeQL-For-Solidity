from src.ast2java.statements.Statement import Statement
from src.ast2java.statements.Block import Block
from src.ast2java.expressions.Expression import Expression


class IfStatement(Statement):
    def __init__(self, _ast, parent, eol):
        super().__init__(_ast, parent, eol)

    def get_content(self):
        result = f"{self.eol}if ({Expression(self.ast.get('condition'), self).get_content()})"
        true_body = self.ast.get('TrueBody')
        result += Block(true_body, self, self.eol).get_content()
        if self.ast.get('FalseBody') is not None:
            result += " else " + Block(self.ast.get('FalseBody'), self, self.eol).get_content()
        return result
