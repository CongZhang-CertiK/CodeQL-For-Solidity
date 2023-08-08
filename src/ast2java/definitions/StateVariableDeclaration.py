from src.ast2java.definitions.ClassElement import ClassElement
from src.ast2java.expressions.VariableDeclaration import VariableDeclaration


class StateVariableDeclaration(ClassElement):
    def __init__(self, ast, parent, in_library=False):
        super().__init__()
        self.ast = ast
        self.parent = parent
        self.in_library = self.parent.ast.get('kind') == 'library'
        self.type = "StateVariableDeclaration"
        self.declarations = []
        self.var_decl_map = {}
        self.eol = "\n\t"
        self.update()

    def get_signature(self):
        return str(self.declarations)

    def update(self):
        for variable_node in self.ast.get("variables"):
            declaration = VariableDeclaration(variable_node, self, self.in_library)
            self.declarations.append(declaration)
            self.var_decl_map[declaration.variable_name] = declaration

    def get_content(self):
        result = super().get_content()
        for variable in self.declarations:
            result += self.eol + variable.get_content()
        return result
