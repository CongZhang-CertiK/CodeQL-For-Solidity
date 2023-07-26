from .Statement import Statement
from .Block import Block
from .Expression import Expression


class UncheckedStatement(Statement):
    def __init__(self, _ast, eol):
        super().__init__(_ast, eol)

    def get_content(self):
        result = f"{self.eol}Boolean unchecked = true;"
        result += f"{self.eol}if(unchecked) "
        result += Block(self.ast.get('body'), self.eol).get_content()
        return result
