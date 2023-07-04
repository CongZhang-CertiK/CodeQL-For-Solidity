from .ClassElement import ClassElement
from .Parameter import Parameter
from src.logger import logger


class FunctionDefinition(ClassElement):

    def __init__(self, compilation_unit, class_type):
        super().__init__()
        self.cu = compilation_unit
        self.class_type = class_type
        self.eol = "\n\t"
        self.java_modifiers = ""
        self.name = self.cu.get('name')
        self.parameters: list[Parameter] = []
        self.return_parameters: list[Parameter] = []
        self.annotations: list[str] = []
        self.body = ""
        self.update_parameters()
        self.update_annotations()
        self.update_java_modifiers()
        self.update_body()

    def update_parameters(self):
        parameter_list = self.cu.get('parameters')
        if type(parameter_list) != list and parameter_list.get('type') == 'ParameterList':
            for parameter in parameter_list.get('parameters'):
                self.parameters.append(Parameter(parameter))
        elif type(parameter_list) == list and len(parameter_list) == 0:
            pass
        else:
            logger.debug("unresolved parameter list: ", type(parameter_list), parameter_list)
        return_parameter_list = self.cu.get('returnParameters')
        if type(return_parameter_list) != list and return_parameter_list.get('type') == 'ParameterList':
            for parameter in return_parameter_list.get('parameters'):
                self.return_parameters.append(Parameter(parameter))
        elif type(return_parameter_list) == list and len(return_parameter_list) == 0:
            pass
        else:
            logger.debug("unresolved return parameter list: ", type(return_parameter_list), return_parameter_list)

    def update_annotations(self):
        visibility = self.cu.get('visibility')
        if visibility is not None:
            self.annotations.append(f"@AccessModifier(\"{visibility}\")")
        mutability = self.cu.get('stateMutability')
        if mutability is not None:
            self.annotations.append(f"@ViewModifier(\"{mutability}\")")

    def update_java_modifiers(self):
        self.java_modifiers = "public void"

    def update_body(self):
        if self.class_type == "class":
            self.body += "{" + self.eol
            self.body += self.eol + "}"
        elif self.class_type == "interface":
            self.body = ";" + self.eol
        else:
            logger.debug("unresolved class type when updating function body")

    def get_content(self):
        result = self.eol
        for annotation in self.annotations:
            result += self.eol
            result += annotation
        result += self.eol
        result += self.java_modifiers + " " + self.name
        result += "("
        param_str = ""
        for param in self.parameters:
            param_str += param.get_content() + ", "
        result += param_str[:-2] + ")"
        result += self.body
        return result
