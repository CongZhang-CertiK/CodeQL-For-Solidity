from .Statement import Statement
from .Block import Block
from .Expression import Expression


class IfStatement(Statement):
    def __init__(self, _ast, eol):
        super().__init__(_ast, eol)

    def get_content(self):
        result = f"{self.eol}if ({Expression(self.ast.get('condition')).get_content()})"
        true_body = self.ast.get('TrueBody')
        result += Block(true_body, self.eol).get_content()
        if self.ast.get('FalseBody') is not None:
            result += " else " + Block(self.ast.get('FalseBody'), self.eol).get_content()
        return result
