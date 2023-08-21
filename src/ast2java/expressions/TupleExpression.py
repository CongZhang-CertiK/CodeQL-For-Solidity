from src.ast2java.expressions.Expression import Expression
from .BaseExpression import BaseExpression


class TupleExpression(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.components = []
        for component in self.ast.get('components'):
            self.components.append(Expression(component, self))

    def get_content(self):
        result = "("
        for component in self.components:
            result += component.get_content()
            if component is not self.components[-1]:
                result += ", "
        result += ")"
        from src.ast2java.statements.ReturnStatement import ReturnStatement
        if type(self.parent) == ReturnStatement and len(self.components) > 1:
            result = "new Result" + result
        return result
