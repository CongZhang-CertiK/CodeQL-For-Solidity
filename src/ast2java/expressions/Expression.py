from src.logger import logger
from src.ast2java.keywordMapping import keyword_map
from .BaseExpression import BaseExpression


def Expression(ast, parent):
    node_type = ast.get('type')
    expression = None
    if node_type == 'stringLiteral':
        from .StringLiteral import StringLiteral
        expression = StringLiteral(ast, parent)
    elif node_type == 'NumberLiteral':
        from .NumberLiteral import NumberLiteral
        expression = NumberLiteral(ast, parent)
    elif node_type == 'BooleanLiteral':
        from .BooleanLiteral import BooleanLiteral
        return BooleanLiteral(ast, parent)
    elif node_type == 'BinaryOperation':
        from .BinaryOperation import BinaryOperation
        expression = BinaryOperation(ast, parent)
    elif node_type == 'UnaryOperation':
        from .UnaryOperation import UnaryOperation
        expression = UnaryOperation(ast, parent)
    elif node_type == 'Identifier':
        from .Identifier import Identifier
        expression = Identifier(ast, parent)
    elif node_type == 'MemberAccess':
        from .MemberAccess import MemberAccess
        expression = MemberAccess(ast, parent)
    elif node_type == 'TupleExpression':
        from .TupleExpression import TupleExpression
        expression = TupleExpression(ast, parent)
    elif node_type == 'IndexAccess':
        from .IndexAccess import IndexAccess
        expression = IndexAccess(ast, parent)
    elif node_type == 'Conditional':
        from .Conditional import Conditional
        expression = Conditional(ast, parent)
    elif node_type == 'NewExpression':
        from .NewExpression import NewExpression
        expression = NewExpression(ast, parent)
    elif node_type == 'FunctionCall':
        from .FunctionCall import FunctionCall
        expression = FunctionCall(ast, parent)
    elif node_type == 'ElementaryTypeName':
        from .ElementaryTypeName import ElementaryTypeName
        expression = ElementaryTypeName(ast, parent)
    else:
        logger.debug('unresolved Expression')
        logger.debug(node_type)
    if expression is not None:
        return expression
    else:
        return BaseExpression(ast, parent).unresolve()
