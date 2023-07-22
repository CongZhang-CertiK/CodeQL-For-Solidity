from .Expression import Expression


class IndexAccess:
    def __init__(self, ast):
        self.ast = ast
        self.base = Expression(self.ast.get('base'))
        self.index = Expression(self.ast.get('index'))

    def get_content(self):
        return f"{self.base.get_content()}.get({self.index.get_content()})"
