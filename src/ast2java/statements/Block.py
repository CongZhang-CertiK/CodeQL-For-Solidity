from src.logger import logger


class Block:
    def __init__(self, _ast, parent, eol, rpd=""):
        self.ast = _ast
        self.parent = parent
        self.eol = eol
        self.rpd = rpd
        self.need_append_return = True

    def get_content(self):
        if self.ast.get('type') == "Block":
            result = "{"
            result += self.rpd
            for statement in self.ast.get('statements'):
                result = self.update_by_statement(statement, result)
            if self.rpd != "" and self.parent.return_statement is not None and self.need_append_return:
                result += self.parent.return_statement
            result += self.eol + "}"
        else:
            result = self.update_by_statement(self.ast, "")
        return result

    def update_by_statement(self, statement, result):
        stmt = None
        if statement.get('type') == "IfStatement":
            from src.ast2java.statements.IfStatement import IfStatement
            stmt = IfStatement(statement, self.parent, self.eol + "\t")
        elif statement.get('type') == "WhileStatement":
            from src.ast2java.statements.WhileStatement import WhileStatement
            stmt = WhileStatement(statement, self.parent, self.eol + "\t")
        elif statement.get('type') == "UncheckedStatement":
            from src.ast2java.statements.UncheckedStatement import UncheckedStatement
            stmt = UncheckedStatement(statement, self.parent, self.eol + "\t")
        elif statement.get('type') == "VariableDeclarationStatement":
            from src.ast2java.statements.VariableDeclarationStatement import VariableDeclarationStatement
            stmt = VariableDeclarationStatement(statement, self.parent, self.eol + "\t")
        elif statement.get('type') == "ExpressionStatement":
            from src.ast2java.statements.ExpressionStatement import ExpressionStatement
            stmt = ExpressionStatement(statement, self.parent, self.eol + "\t")
        elif statement.get('type') == "EmitStatement":
            from src.ast2java.statements.EmitStatement import EmitStatement
            stmt = EmitStatement(statement, self.parent, self.eol + "\t")
        elif statement.get('type') == "ReturnStatement":
            from src.ast2java.statements.ReturnStatement import ReturnStatement
            stmt = ReturnStatement(statement, self.parent, self.eol + "\t")
            self.need_append_return = False
        elif statement.get('type') == "RevertStatement":
            from src.ast2java.statements.RevertStatement import RevertStatement
            stmt = RevertStatement(statement, self.parent, self.eol + "\t")
        elif statement.get('type') == "BreakStatement":
            result += "\tbreak;"
        elif statement.get('type') == "InLineAssemblyStatement":
            from src.ast2java.statements.InLineAssemblyStatement import InLineAssemblyStatement
            stmt = InLineAssemblyStatement(statement, self.parent, self.eol + "\t")
        else:
            logger.debug("unresolved statement: " + statement.get('type'))
        if stmt is not None:
            result += stmt.get_content()
        return result
