from src.ast2java.expressions.Expression import Expression


class NewExpression:
    def __init__(self, ast):
        self.ast = ast
        self.type_name = Expression(self.ast.get('typeName'))

    def get_content(self):
        return f"new {self.type_name.get_content()}"
