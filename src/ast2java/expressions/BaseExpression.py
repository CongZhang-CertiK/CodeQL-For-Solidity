class BaseExpression:
    def __init__(self, ast, parent):
        self.ast = ast
        self.parent = parent
        self.resolved = True

    def unresolve(self):
        self.resolved = False

    def get_content(self):
        return "UnresolvedExpression:get_content"

    def get_exp_type(self):
        return "UnresolvedExpression:get_exp_type"

    def find_contract(self):
        if not self.resolved:
            return None
        search = self.parent
        from src.ast2java.definitions.JavaSourceFile import JavaSourceFile
        while type(search) is not JavaSourceFile:
            search = search.parent
        return search

    def find_function(self):
        if not self.resolved:
            return None
        search = self.parent
        from src.ast2java.definitions.FunctionDefinition import FunctionDefinition
        from src.ast2java.definitions.JavaSourceFile import JavaSourceFile
        while type(search) is not FunctionDefinition:
            search = search.parent
            if type(search) is JavaSourceFile:
                return None
        return search

    def get_func_param(self):
        function = self.find_function()
        result = {}
        if function is None:
            return result
        for param in function.parameters:
            result[param.name] = param
        return result
