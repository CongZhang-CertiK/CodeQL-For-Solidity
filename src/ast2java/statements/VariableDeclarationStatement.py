from src.ast2java.expressions.VariableDeclaration import VariableDeclaration
from src.ast2java.statements.Statement import Statement
from src.ast2java.expressions.Expression import Expression


class VariableDeclarationStatement(Statement):
    def __init__(self, ast, eol):
        super().__init__(ast, eol)
        self.variables = []
        for variable in self.ast.get('variables'):
            self.variables.append(VariableDeclaration(variable))
        if self.ast.get('initialValue') is None:
            self.initial_value = None
        else:
            self.initial_value = Expression(self.ast.get('initialValue'))

    def get_content(self):
        result = self.eol
        for variable in self.variables:
            result += variable.get_content()[:-1]
            if variable is not self.variables[-1]:
                result += ", "
        if self.initial_value is not None:
            result += " = "
            result += self.initial_value.get_content()
        result += ";"
        return result
