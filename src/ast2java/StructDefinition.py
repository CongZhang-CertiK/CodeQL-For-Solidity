from .ClassElement import ClassElement
from .VariableDeclaration import VariableDeclaration
from src.logger import logger


class StructDefinition(ClassElement):
    def __init__(self, ast):
        super().__init__()
        self.ast = ast
        self.eol = "\n\t"
        self.name = self.ast.get('name')
        self.sub_variable_declarations = []
        self.update_members()

    def get_signature(self):
        return str(self.sub_variable_declarations)

    def update_members(self):
        for member in self.ast.get('members'):
            if member.get('type') == "VariableDeclaration":
                self.sub_variable_declarations.append(VariableDeclaration(member))
            else:
                logger.debug("unresolved StructDefinition member: " + member)

    def get_content(self):
        result = super().get_content()
        result += f"{self.eol}@struct"
        result += f"{self.eol}public class {self.name} {{"
        for member in self.sub_variable_declarations:
            member.visibility = "public"
            result += f"{self.eol}\t{member.get_content()}"
        result += self.eol + "}"
        return result
