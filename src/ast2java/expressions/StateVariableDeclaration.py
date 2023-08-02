from src.ast2java.definitions.ClassElement import ClassElement
from .VariableDeclaration import VariableDeclaration


class StateVariableDeclaration(ClassElement):
    def __init__(self, ast, in_library=False):
        super().__init__()
        self.ast = ast
        self.in_library = in_library
        self.type = "StateVariableDeclaration"
        self.declarations = []
        self.eol = "\n\t"
        self.update()

    def get_signature(self):
        return str(self.declarations)

    def update(self):
        for variable_node in self.ast.get("variables"):
            self.declarations.append(VariableDeclaration(variable_node, self.in_library))

    def get_content(self):
        result = super().get_content()
        for variable in self.declarations:
            result += self.eol + variable.get_content()
        return result
