from .Statement import Statement
from .Block import Block
from .Expression import Expression


class WhileStatement(Statement):
    def __init__(self, _ast, eol):
        super().__init__(_ast, eol)

    def get_content(self):
        result = f"{self.eol}while ({Expression(self.ast.get('condition')).get_content()})"
        result += Block(self.ast.get('body'), self.eol).get_content()
        return result
