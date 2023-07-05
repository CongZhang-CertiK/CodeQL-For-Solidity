from .ClassElement import ClassElement
from .VariableDeclaration import VariableDeclaration
from .Expression import Expression
from src.logger import logger


class StateVariableDeclaration(ClassElement):
    def __init__(self, ast):
        super().__init__()
        self.ast = ast
        self.declarations = []
        self.eol = "\n\t"
        self.update()

    def update(self):
        for variable_node in self.ast.get("variables"):
            self.declarations.append(VariableDeclaration(variable_node))

    def get_content(self):
        result = ""
        for variable in self.declarations:
            result += self.eol + variable.get_content()
        return result
