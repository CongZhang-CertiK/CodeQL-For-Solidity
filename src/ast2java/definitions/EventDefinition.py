from src.ast2java.definitions.ClassElement import ClassElement
from src.ast2java.definitions.Parameter import Parameter


class EventDefinition(ClassElement):
    def __init__(self, ast, parent):
        super().__init__()
        self.parent = parent
        self.ast = ast
        self.eol = "\n\t"
        self.name = self.ast.get('name')
        self.parameters = []
        self.update_members()

    def get_signature(self):
        return str(self.parameters)

    def update_members(self):
        parameter_list = self.ast.get('parameters')
        if type(parameter_list) != list and parameter_list.get('type') == 'ParameterList':
            for parameter in parameter_list.get('parameters'):
                self.parameters.append(Parameter(parameter))

    def get_content(self):
        result = super().get_content()
        result += f"{self.eol}@event"
        result += f"{self.eol}public void {self.name}("
        for parameter in self.parameters:
            result += f"{self.eol}\t{parameter.get_content()},"
        result = result[:-1] + self.eol + ")"
        if self.parent.class_type != "interface":
            result += "{}"
        result += ";"
        return result
