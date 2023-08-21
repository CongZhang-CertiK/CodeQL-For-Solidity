from src.ast2java.definitions.ClassElement import ClassElement
from src.ast2java.expressions.VariableDeclaration import VariableDeclaration
from src.logger import logger


class StructDefinition(ClassElement):
    def __init__(self, ast, parent):
        super().__init__()
        self.ast = ast
        self.parent = parent
        self.eol = "\n\t"
        self.name = self.ast.get('name')
        self.sub_variable_declarations = []
        self.update_members()

    def get_signature(self):
        return str(self.sub_variable_declarations)

    def update_members(self):
        for member in self.ast.get('members'):
            if member.get('type') == "VariableDeclaration":
                self.sub_variable_declarations.append(VariableDeclaration(member, self))
            else:
                logger.debug("unresolved StructDefinition member: " + member)

    def get_constructor(self):
        param_str = ""
        body_str = ""
        for index in range(0, len(self.sub_variable_declarations)):
            member = self.sub_variable_declarations[index]
            param_str += f"{member.variable_type.name} p{index}"
            if member is not self.sub_variable_declarations[-1]:
                param_str += ", "
            body_str += f"{self.eol}\t\t{member.variable_name} = p{index};"
        return f"{self.eol}\t{self.name}({param_str}){{" \
               f"{body_str}" \
               f"{self.eol}\t}}"

    def get_content(self):
        result = super().get_content()
        result += f"{self.eol}@struct"
        result += f"{self.eol}public class {self.name} {{"
        for member in self.sub_variable_declarations:
            member.visibility = "public"
            result += f"{self.eol}\t{member.get_content()}"
        result += self.get_constructor()
        result += self.eol + "}"
        return result
