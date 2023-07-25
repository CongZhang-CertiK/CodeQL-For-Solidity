class Block:
    def __init__(self, _ast, eol):
        self.ast = _ast
        self.eol = eol

    def get_content(self):
        result = "{"
        for statement in self.ast.get('statements'):
            stmt = None
            if statement.get('type') == "IfStatement":
                from .IfStatement import IfStatement
                stmt = IfStatement(statement, self.eol+"\t")
            elif statement.get('type') == "VariableDeclarationStatement":
                from .VariableDeclarationStatement import VariableDeclarationStatement
                stmt = VariableDeclarationStatement(statement, self.eol+"\t")
            elif statement.get('type') == "ExpressionStatement":
                from .ExpressionStatement import ExpressionStatement
                stmt = ExpressionStatement(statement, self.eol+"\t")
            else:
                if statement.get('type') in [
                    'stringLiteral',
                    'NumberLiteral',
                    'BooleanLiteral',
                    'BinaryOperation',
                    'UnaryOperation',
                    'Identifier',
                    'MemberAccess',
                    'TupleExpression',
                    'IndexAccess',
                    'FunctionCall'
                ]:
                    from .Expression import Expression
                    result += self.eol + "\treturn " + Expression(statement).get_content() + ";"
                else:
                    result += self.eol + "\t" + statement.get('type')
            if stmt is not None:
                result += stmt.get_content()
        result += self.eol + "}"
        return result

