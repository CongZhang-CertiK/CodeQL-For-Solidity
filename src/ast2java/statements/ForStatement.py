from src.ast2java.statements.Statement import Statement
from src.ast2java.statements.Block import Block
from src.ast2java.expressions.Expression import Expression


class ForStatement(Statement):
    def __init__(self, _ast, parent, eol):
        super().__init__(_ast, parent, eol)
        self.init_expression = None
        self.condition_expression = None
        self.loop_expression = None
        if self.ast.get('initExpression') is not None:
            self.init_expression = Block(self.ast.get('initExpression'), self, "")
        if self.ast.get('conditionExpression') is not None:
            self.condition_expression = Expression(self.ast.get('conditionExpression'), self)
        if self.ast.get('conditionExpression') is not None:
            self.loop_expression = Block(self.ast.get('loopExpression'), self, "")

    def get_content(self):
        result = f"{self.eol}for ("
        if self.init_expression is not None:
            result += f"{self.init_expression.get_content()}"
        else:
            result += ";"
        if self.condition_expression is not None:
            result += f"{self.condition_expression.get_content()}"
        result += ";"
        if self.loop_expression is not None:
            result += f"{self.loop_expression.get_content()[:-1]}"
        else:
            result += ";"
        result += f")"
        result += Block(self.ast.get('body'), self, self.eol).get_content()
        return result
