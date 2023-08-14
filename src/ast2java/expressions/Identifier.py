from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map
from .BaseExpression import BaseExpression


class Identifier(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.name = self.ast.get('name')
        self.contract = self.find_contract()
        self.func_param = self.get_func_param()
        self.var_type = ""

    def get_content(self):
        result = self.name
        if self.name == '_':
            result = "_function_body()"
        return result

    def get_exp_type(self):
        if self.name in self.func_param:
            self.var_type = self.func_param[self.name].type_name
        elif self.name in self.contract.declarations.keys():
            self.var_type = self.contract.declarations[self.name].variable_type.name
        else:
            self.var_type = "UnresolvedIdentifier:get_exp_type: " + self.name
        return self.var_type
