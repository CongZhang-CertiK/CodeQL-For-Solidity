from src.ast2java.definitions.ClassElement import ClassElement
from .VariableDeclaration import VariableDeclaration
from .BaseExpression import BaseExpression


class StateVariableDeclaration(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.in_library = self.parent.ast.get('kind') == 'library'
        self.type = "StateVariableDeclaration"
        self.declarations = []
        self.eol = "\n\t"
        self.update()

    def get_signature(self):
        return str(self.declarations)

    def update(self):
        for variable_node in self.ast.get("variables"):
            self.declarations.append(VariableDeclaration(variable_node, self, self.in_library))

    def get_content(self):
        result = super().get_content()
        for variable in self.declarations:
            result += self.eol + variable.get_content()
        return result
