from .Statement import Statement
from .Block import Block
from .Expression import Expression


class EmitStatement(Statement):
    def __init__(self, _ast, eol):
        super().__init__(_ast, eol)

    def get_content(self):
        result = f"{self.eol}{Expression(self.ast.get('eventCall')).get_content()};"
        return result
