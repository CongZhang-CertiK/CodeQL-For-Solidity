from src.logger import logger
from src.ast2java.keywordMapping import keyword_map


class Expression:
    def __init__(self, ast_node):
        self.ast = ast_node
        self.node_type = self.ast.get('type')

    def get_content(self):
        if self.node_type == 'stringLiteral':
            return '"' + self.ast.get('value') + '"'
        elif self.node_type == 'NumberLiteral':
            return f"_uint({self.ast.get('number')})"
        elif self.node_type == 'BooleanLiteral':
            return keyword_map(str(self.ast.get('value')))
        elif self.node_type == 'BinaryOperation':
            from .BinaryOperation import BinaryOperation
            return BinaryOperation(self.ast).get_content()
        elif self.node_type == 'UnaryOperation':
            from .UnaryOperation import UnaryOperation
            return UnaryOperation(self.ast).get_content()
        elif self.node_type == 'Identifier':
            return self.ast.get('name')
        elif self.node_type == 'MemberAccess':
            from .MemberAccess import MemberAccess
            return MemberAccess(self.ast).get_content()
        elif self.node_type == 'TupleExpression':
            from .TupleExpression import TupleExpression
            return TupleExpression(self.ast).get_content()
        elif self.node_type == 'IndexAccess':
            from .IndexAccess import IndexAccess
            return IndexAccess(self.ast).get_content()
        elif self.node_type == 'Conditional':
            from .Conditional import Conditional
            return Conditional(self.ast).get_content()
        elif self.node_type == 'NewExpression':
            from .NewExpression import NewExpression
            return NewExpression(self.ast).get_content()
        elif self.node_type == 'FunctionCall':
            from .FunctionCall import FunctionCall
            return FunctionCall(self.ast).get_content()
        elif self.node_type == 'ElementaryTypeName':
            return keyword_map(self.ast.get('name'))
        else:
            logger.debug('unresolved Expression')
            logger.debug(self.node_type)
            return self.node_type
