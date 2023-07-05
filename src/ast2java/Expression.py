from src.logger import logger


class Expression:
    def __init__(self, ast_node):
        self.ast = ast_node
        self.node_type = self.ast.get('type')

    def get_content(self):
        if self.node_type == 'stringLiteral':
            return '"' + self.ast.get('value') + '"'
        elif self.node_type == 'NumberLiteral':
            return self.ast.get('number')
        elif self.node_type == "FunctionCall":
            return "FunctionCall"
        else:
            logger.debug('unresolved Expression')
            logger.debug(self.node_type)
