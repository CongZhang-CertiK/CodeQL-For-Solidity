from src.ast2java.definitions.ClassElement import ClassElement
from src.ast2java.definitions.Parameter import Parameter
from src.ast2java.expressions.Expression import Expression


class CustomErrorDefinition(ClassElement):
    def __init__(self, ast, parent):
        super().__init__()
        self.parent = parent
        self.ast = ast
        self.eol = "\n\t"
        self.name = Expression(self.ast.get('name'), parent).get_content()
        self.parameters = []
        self.update_members()

    def get_signature(self):
        return f"{self.name}({str(self.parameters)})"

    def update_members(self):
        parameter_list = self.ast.get('parameterList')
        if type(parameter_list) != list and parameter_list.get('type') == 'ParameterList':
            for parameter in parameter_list.get('parameters'):
                self.parameters.append(Parameter(parameter))

    def get_content(self):
        result = super().get_content()
        result += f"{self.eol}@error"
        result += f"{self.eol}public void {self.name}("
        for parameter in self.parameters:
            result += f"{self.eol}\t{parameter.get_content()}"
            if parameter is not self.parameters[-1]:
                result += ","
        result += self.eol + ")"
        if self.parent.class_type != "interface":
            result += "{}"
        result += ";"
        return result
