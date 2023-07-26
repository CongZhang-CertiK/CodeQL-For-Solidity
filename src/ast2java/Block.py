class Block:
    def __init__(self, _ast, eol):
        self.ast = _ast
        self.eol = eol

    def get_content(self):
        if self.ast.get('type') == "Block":
            result = "{"
            for statement in self.ast.get('statements'):
                result = self.update_by_statement(statement, result)
            result += self.eol + "}"
        else:
            result = self.update_by_statement(self.ast, "")
        return result

    def update_by_statement(self, statement, result):
        stmt = None
        if statement.get('type') == "IfStatement":
            from .IfStatement import IfStatement
            stmt = IfStatement(statement, self.eol + "\t")
        elif statement.get('type') == "WhileStatement":
            from .WhileStatement import WhileStatement
            stmt = WhileStatement(statement, self.eol + "\t")
        elif statement.get('type') == "UncheckedStatement":
            from .UncheckedStatement import UncheckedStatement
            stmt = UncheckedStatement(statement, self.eol + "\t")
        elif statement.get('type') == "VariableDeclarationStatement":
            from .VariableDeclarationStatement import VariableDeclarationStatement
            stmt = VariableDeclarationStatement(statement, self.eol + "\t")
        elif statement.get('type') == "ExpressionStatement":
            from .ExpressionStatement import ExpressionStatement
            stmt = ExpressionStatement(statement, self.eol + "\t")
        elif statement.get('type') == "EmitStatement":
            from .EmitStatement import EmitStatement
            stmt = EmitStatement(statement, self.eol + "\t")
        elif statement.get('type') == "ReturnStatement":
            from .ReturnStatement import ReturnStatement
            stmt = ReturnStatement(statement, self.eol + "\t")
        elif statement.get('type') == "BreakStatement":
            result += "\tbreak;"
        if stmt is not None:
            result += stmt.get_content()
        return result
