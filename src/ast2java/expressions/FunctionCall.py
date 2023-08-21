from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map
from src.logger import logger
from .BaseExpression import BaseExpression
from src.ast2java.compilationGlobal import compilation_global


class FunctionCall(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        if type(self.ast.get('expression')) == str:
            self.expression = self.ast.get('expression')
        else:
            self.expression = Expression(self.ast.get('expression'), self).get_content()
        self.arguments = []
        for argument in self.ast.get('arguments'):
            self.arguments.append(Expression(argument, self))
        self.contract = self.find_contract()
        self.function_definition = self.find_function()
        # if self.function_definition is not None:
        #     logger.info(self.function_definition.name)

    def find_function(self):
        function_defs = self.contract.functions
        if self.expression in function_defs.keys():
            return function_defs[self.expression]
        return None

    def get_content(self):
        result = f"{keyword_map(self.expression, function=True)}("
        for index in range(0, len(self.arguments)):
            argument = self.arguments[index]
            logger.info(argument.get_exp_type() + ": " + argument.get_content())
            result += argument.get_content()
            if self.expression == "type":
                result += ".class"
            if argument != self.arguments[-1]:
                result += ", "
        result += ")"
        if self.expression in compilation_global['__reorged_list']:
            result = "new " + result
        return result

    def get_exp_type(self):
        return "FunctionCall"
