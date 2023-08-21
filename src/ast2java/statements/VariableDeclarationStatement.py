from src.ast2java.expressions.VariableDeclaration import VariableDeclaration
from src.ast2java.statements.Statement import Statement
from src.ast2java.expressions.Expression import Expression
from src.logger import logger


class VariableDeclarationStatement(Statement):
    def __init__(self, _ast, parent, eol):
        super().__init__(_ast, parent, eol)
        self.variables = []
        for variable in self.ast.get('variables'):
            if variable is None:
                continue
            self.variables.append(VariableDeclaration(variable, self))
        if self.ast.get('initialValue') is None:
            self.initial_value = None
        else:
            self.initial_value = Expression(self.ast.get('initialValue'), self)

    def get_content(self):
        if len(self.variables) == 1:
            if self.initial_value is not None:
                result = f"{self.eol}{self.variables[0].get_content()[:-1]} = {self.initial_value.get_content()};"
            else:
                result = f"{self.eol}{self.variables[0].get_content()[:-1]} = null;"
        else:
            from src.ast2java.expressions.TupleExpression import TupleExpression
            from src.ast2java.expressions.FunctionCall import FunctionCall
            if type(self.initial_value) == TupleExpression:
                result = ""
                if len(self.variables) != len(self.initial_value.components):
                    logger.debug("TODO VariableDeclarationStatement")
                    return "TODO VariableDeclarationStatement"
                for index in range(0, len(self.variables)):
                    variable = self.variables[index]
                    component = self.initial_value.components[index].get_content()
                    result += f"{self.eol}" \
                              f"{variable.get_content()[:-1]} = {component};"
            elif type(self.initial_value) == FunctionCall:
                result = f"{self.eol}Result result = {self.initial_value.get_content()};"
                for index in range(0, len(self.variables)):
                    variable = self.variables[index]
                    from src.ast2java.keywordMapping import keyword_map
                    type_cast = keyword_map(variable.variable_type.name, function=True)
                    component = f"{type_cast}(result.get({index}))"
                    result += f"{self.eol}" \
                              f"{variable.get_content()[:-1]} = {component};"
            else:
                logger.debug("unknown Expression Type at VariableDeclarationStatement: " + type(self.initial_value))
                result = type(self.initial_value)
        return result
