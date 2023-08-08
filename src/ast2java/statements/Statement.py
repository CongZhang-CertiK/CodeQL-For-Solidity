class Statement:
    def __init__(self, _ast, parent, eol):
        self.ast = _ast
        self.parent = parent
        self.type = self.ast.get('type')
        self.eol = eol

    def get_content(self):
        return self.eol + self.type

