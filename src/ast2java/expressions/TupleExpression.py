from src.ast2java.expressions.Expression import Expression


class TupleExpression:
    def __init__(self, ast):
        self.ast = ast
        self.components = []
        for component in self.ast.get('components'):
            self.components.append(Expression(component))

    def get_content(self):
        result = "("
        for component in self.components:
            result += component.get_content()
            if component != self.components[-1]:
                result += ", "
        result += ")"
        return result
