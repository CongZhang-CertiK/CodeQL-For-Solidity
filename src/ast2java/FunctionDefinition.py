from .ClassElement import ClassElement
from .Parameter import Parameter
from src.logger import logger
from src.ast2java.keywordMapping import keyword_map


class FunctionDefinition(ClassElement):

    def __init__(self, ast, parent):
        super().__init__()
        self.ast = ast
        self.parent = parent
        self.class_type = parent.class_type
        self.eol = "\n\t"
        self.java_modifiers = ""
        self.name = self.ast.get('name')
        self.parameters: list[Parameter] = []
        self.return_parameters: list[Parameter] = []
        self.annotations: list[str] = []
        self.body_ast = self.ast.get('body')
        self.body = ""
        self.visibility = ""
        self.is_receive = self.ast.get('isReceive')
        self.is_fallback = self.ast.get('isFallback')
        self.is_constructor = self.ast.get('isConstructor')
        self.sol_modifiers = self.ast.get('modifiers')
        self.update_parameters()
        self.update_annotations()
        self.update_java_modifiers()
        self.update_body()

    def update_parameters(self):
        parameter_list = self.ast.get('parameters')
        if type(parameter_list) != list and parameter_list.get('type') == 'ParameterList':
            for parameter in parameter_list.get('parameters'):
                self.parameters.append(Parameter(parameter))
        elif type(parameter_list) == list and len(parameter_list) == 0:
            pass
        else:
            logger.debug("unresolved parameter list: ", type(parameter_list), parameter_list)

        return_parameter_list = self.ast.get('returnParameters')
        if type(return_parameter_list) != list and return_parameter_list.get('type') == 'ParameterList':
            for parameter in return_parameter_list.get('parameters'):
                self.return_parameters.append(Parameter(parameter))
        elif type(return_parameter_list) == list and len(return_parameter_list) == 0:
            pass
        else:
            logger.debug("unresolved return parameter list: ", type(return_parameter_list), return_parameter_list)

    def update_annotations(self):
        visibility = self.ast.get('visibility')
        if visibility is not None and visibility != "default":
            self.annotations.append(f"@{keyword_map(visibility)}")
            if visibility == "public" or visibility == "external":
                self.visibility = "public"
            else:
                self.visibility = "private"
        mutability = self.ast.get('stateMutability')
        if mutability is not None:
            self.annotations.append(f"@{keyword_map(mutability)}")
        if self.ast.get('isVirtual'):
            self.annotations.append(f"@virtual")

    def update_java_modifiers(self):
        if self.name == "constructor":
            self.name = self.parent.class_name
            self.java_modifiers = ""
        else:
            if len(self.return_parameters) == 0:
                self.java_modifiers = f"{self.visibility} void "
            elif len(self.return_parameters) == 1:
                self.java_modifiers = f"{self.visibility} {self.return_parameters[0].get_content()} "
            else:
                self.java_modifiers = f"{self.visibility} TODO "

    def update_body(self):
        if len(self.body_ast) != 0:
            self.body += "{" + self.eol
            self.body += self.eol + "}"
        else:
            self.body = ";" + self.eol

    def get_content(self):
        result = self.eol
        for annotation in self.annotations:
            result += self.eol
            result += annotation
        result += self.eol
        result += self.java_modifiers + self.name
        result += "("
        param_str = ""
        for param in self.parameters:
            param_str += param.get_content() + ", "
        result += param_str[:-2] + ")"
        result += self.body
        return result
