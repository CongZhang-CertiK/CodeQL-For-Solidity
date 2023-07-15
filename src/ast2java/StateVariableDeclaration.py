from .ClassElement import ClassElement
from .VariableDeclaration import VariableDeclaration
from .Expression import Expression
from src.logger import logger


class StateVariableDeclaration(ClassElement):
    def __init__(self, ast):
        super().__init__()
        self.ast = ast
        self.type = "StateVariableDeclaration"
        self.declarations = []
        self.inherit_from = None
        self.eol = "\n\t"
        self.update()

    def update(self):
        for variable_node in self.ast.get("variables"):
            self.declarations.append(VariableDeclaration(variable_node))

    def get_content(self):
        result = self.eol
        for variable in self.declarations:
            if self.inherit_from is not None:
                result += self.eol + f"@inherit(\"{self.inherit_from}\")"
            result += self.eol + variable.get_content()
        return result
