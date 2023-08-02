from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map


class FunctionCall:
    def __init__(self, ast):
        self.ast = ast
        if type(self.ast.get('expression')) == str:
            self.expression = self.ast.get('expression')
        else:
            self.expression = Expression(self.ast.get('expression')).get_content()
        self.arguments = []
        for argument in self.ast.get('arguments'):
            self.arguments.append(Expression(argument))

    def get_content(self):
        result = f"{keyword_map(self.expression, function=True)}("
        for argument in self.arguments:
            result += argument.get_content()
            if argument != self.arguments[-1]:
                result += ", "
        result += ")"
        return result
