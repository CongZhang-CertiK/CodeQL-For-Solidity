from .AssemblyExpression import AssemblyExpression


class AssemblyLocalDefinition:
    def __init__(self, ast, eol):
        self.ast = ast
        self.eol = eol

    def get_content(self):
        result = f"{self.eol}"
        names_content = ""
        names = self.ast.get('names')
        for name in names:
            names_content += "uint256 " + AssemblyExpression(name).get_content()
            if name is not names[-1]:
                names_content += ", "
        result += names_content
        result += " = "
        result += AssemblyExpression(self.ast.get('expression')).get_content()
        result += ";"
        return result
