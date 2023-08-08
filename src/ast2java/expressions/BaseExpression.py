class BaseExpression:
    def __init__(self, ast, parent):
        self.ast = ast
        self.parent = parent
        self.resolved = True

    def unresolve(self):
        self.resolved = False

    def get_content(self):
        return "UnresolvedExpression"

    def get_exp_type(self):
        return "UnresolvedExpression"

    def find_contract(self):
        if not self.resolved:
            return None
        search = self.parent
        from src.ast2java.definitions.JavaSourceFile import JavaSourceFile
        while type(search) is not JavaSourceFile:
            search = search.parent
        return search
