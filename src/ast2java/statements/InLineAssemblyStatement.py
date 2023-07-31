from src.ast2java.statements.Statement import Statement
from src.ast2java.assembly.AssemblyBlock import AssemblyBlock
from src.ast2java.expressions.Expression import Expression


class InLineAssemblyStatement(Statement):
    def __init__(self, _ast, eol):
        super().__init__(_ast, eol)

    def get_content(self):
        result = f"{self.eol}_assembly_start();"
        result += f"{self.eol}"
        result += AssemblyBlock(self.ast.get('body'), self.eol).get_content()
        return result
