from .ClassElement import ClassElement
from src.logger import logger


class EnumDefinition(ClassElement):
    def __init__(self, ast):
        super().__init__()
        self.ast = ast
        self.eol = "\n\t"
        self.name = self.ast.get('name')
        self.members: list[str] = []
        self.update_members()

    def get_signature(self):
        return str(self.members)

    def update_members(self):
        for member in self.ast.get('members'):
            if member.get('type') == 'EnumValue':
                self.members.append(member.get('name'))
            else:
                logger.debug("unresolved EnumMember: " + member)

    def get_content(self):
        result = super().get_content()
        result += f"{self.eol}enum {self.name} {{"
        for member in self.members:
            result += f"{self.eol}\t{member},"
        result = result[:-1] + self.eol + "}"
        return result
