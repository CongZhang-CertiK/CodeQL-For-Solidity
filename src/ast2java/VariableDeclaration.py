from src.logger import logger
from src.ast2java.keywordMapping import keyword_map, resolve_type
from .Expression import Expression


class VariableDeclaration:
    class VariableType:
        def __init__(self, ast_node):
            self.ast = ast_node
            self.node_type = self.ast.get('type')
            self.name = resolve_type(self.ast)

    def __init__(self, ast_node):
        self.ast = ast_node
        self.variable_node_type = self.ast.get('type')
        self.variable_type = self.VariableType(self.ast.get('typeName'))
        self.variable_name = self.ast.get('name')
        self.has_expression = False
        if self.ast.get('expression') is not None:
            self.has_expression = True
            self.expression = Expression(self.ast.get('expression'))
        self.visibility = self.ast.get('visibility')
        self.is_state_var = self.ast.get('isStateVar')
        self.is_const = self.ast.get('isDeclaredConst')
        self.is_indexed = self.ast.get('isIndexed')

    def get_content(self):
        if self.variable_node_type == "VariableDeclaration":
            result = ""
            if self.visibility is not None:
                result += self.visibility
            if self.is_const is not None and self.is_const:
                result += " final"
            result += " " + self.variable_type.name
            result += " " + self.variable_name
            if self.has_expression is not None and self.has_expression:
                result += f" = new {self.variable_type.name}({self.expression.get_content()})"
            result += ";"
            return result
        else:
            logger.debug("unresolved VariableDeclaration")
            logger.debug(self.variable_node_type)
