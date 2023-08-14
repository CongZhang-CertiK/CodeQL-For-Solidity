from src.ast2java.definitions.ClassElement import ClassElement
from src.ast2java.definitions.Parameter import Parameter
from src.ast2java.statements.Block import Block
from src.logger import logger
from src.ast2java.keywordMapping import keyword_map


class FunctionDefinition(ClassElement):

    def __init__(self, ast, parent):
        super().__init__()
        self.ast = ast
        self.type = "FunctionDefinition"
        self.implement = None
        self.parent = parent
        self.class_type = parent.class_type
        self.eol = "\n\t"
        self.java_modifiers = ""
        self.return_type = None
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

    def get_signature(self):
        result = self.name
        result += "("
        param_str = ""
        for param in self.parameters:
            param_str += param.get_content() + ", "
        result += param_str[:-2] + ")"
        return result

    def update_parameters(self):
        parameter_list = self.ast.get('parameters')
        if type(parameter_list) != list and parameter_list.get('type') == 'ParameterList':
            for parameter in parameter_list.get('parameters'):
                self.parameters.append(Parameter(parameter))
        elif type(parameter_list) == list and len(parameter_list) == 0:
            pass
        else:
            logger.debug("unresolved parameter list: " + type(parameter_list) + parameter_list)

        return_parameter_list = self.ast.get('returnParameters')
        if type(return_parameter_list) != list and return_parameter_list.get('type') == 'ParameterList':
            for parameter in return_parameter_list.get('parameters'):
                self.return_parameters.append(Parameter(parameter))
        elif type(return_parameter_list) == list and len(return_parameter_list) == 0:
            pass
        else:
            logger.debug("unresolved return parameter list: " + type(return_parameter_list) + return_parameter_list)

    def update_annotations(self):
        visibility = self.ast.get('visibility')
        if visibility is not None and visibility != "default":
            self.annotations.append(f"@{keyword_map(visibility)}")
            if visibility == "public" or visibility == "external":
                self.visibility = "public"
                if self.parent.ast.get('kind') == "library":
                    self.visibility += " static"
            else:
                self.visibility = "private"
                if self.parent.ast.get('kind') == "library":
                    self.visibility = "public static"
        mutability = self.ast.get('stateMutability')
        if mutability is not None:
            self.annotations.append(f"@{keyword_map(mutability)}")
        if self.ast.get('isVirtual'):
            self.annotations.append(f"@virtual")
        for modifier in self.sol_modifiers:
            self.annotations.append(f"@{modifier.get('name')}")

    def update_java_modifiers(self):
        if self.name == "constructor":
            self.name = self.parent.class_name
            self.java_modifiers = ""
        else:
            self.return_type = None
            if len(self.return_parameters) == 0:
                self.return_type = 'void'
            elif len(self.return_parameters) == 1:
                self.return_type = self.return_parameters[0].type_name
            else:
                self.return_type = 'TODO'
            self.java_modifiers = f"{self.visibility} {self.return_type} "

    def update_body(self):
        if len(self.body_ast) == 0:
            self.body = ";"
            return
        if self.body_ast.get('type') == 'Block':
            return_param_decl = ""
            for param in self.return_parameters:
                if param.name is None:
                    continue
                return_param_decl += f"{self.eol}\t{param.type_name} {param.name} = null;"
            self.body += Block(self.body_ast, self, self.eol, return_param_decl).get_content()

    def get_content(self):
        result = ""
        for annotation in self.annotations:
            result += self.eol
            result += annotation
        if self.implement is not None:
            result += f"{self.eol}@implement(\"{self.implement}\")"
        result += super().get_content()
        result += self.eol + self.java_modifiers + self.get_signature()
        result += self.body
        return result
