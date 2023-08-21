from src.ast2java.expressions.Expression import Expression
from src.ast2java.keywordMapping import keyword_map
from .BaseExpression import BaseExpression


class BinaryOperation(BaseExpression):
    def __init__(self, ast, parent):
        super().__init__(ast, parent)
        self.left = Expression(self.ast.get('left'), self)
        self.right = Expression(self.ast.get('right'), self)
        self.operator = self.ast.get('operator')

    def get_content(self):
        from src.ast2java.expressions.TupleExpression import TupleExpression
        if self.operator == "=" and type(self.left) == TupleExpression:
            return self.get_tuple_assign()
        evm_op = keyword_map(self.operator)
        if evm_op != self.operator:
            return f"{evm_op}({self.left.get_content()}, {self.right.get_content()})"
        else:
            from .IndexAccess import IndexAccess
            if type(self.left) == IndexAccess and self.operator == "=":
                return f"{self.left.base.get_content()}" \
                       f".put({self.left.index.get_content()}, {self.right.get_content()})"
            return f"{self.left.get_content()} {self.operator} {self.right.get_content()}"

    def get_tuple_assign(self):
        components = ""
        for component in self.left.components:
            components += component.get_content()
            if component is not self.left.components[-1]:
                components += ", "
        return f"_assign({components}, {self.right.get_content()})"
