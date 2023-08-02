from src.logger import logger
from src.ast2java.keywordMapping import keyword_map


class AssemblyExpression:
    def __init__(self, ast_node):
        self.ast = ast_node
        self.node_type = self.ast.get('type')

    def get_content(self):
        if self.node_type == 'Identifier':
            return self.ast.get('name')
        elif self.node_type == 'DecimalNumber':
            return f"_uint({self.ast.get('value')})"
        elif self.node_type == 'AssemblyExpression':
            arguments = self.ast.get('arguments')
            if len(arguments) == 0:
                return self.ast.get('functionName')
            else:
                arguments_content = ""
                for argument in arguments:
                    arguments_content += AssemblyExpression(argument).get_content()
                    if argument is not arguments[-1]:
                        arguments_content += ", "
                return f"{self.ast.get('functionName')}({arguments_content})"
        else:
            logger.debug('unresolved AssemblyExpression')
            logger.debug(self.node_type)
            return self.node_type
