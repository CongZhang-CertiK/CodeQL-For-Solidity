class Statement:
    def __init__(self, _ast, eol):
        self.ast = _ast
        self.type = self.ast.get('type')
        self.eol = eol

    def get_content(self):
        return self.eol + self.type

