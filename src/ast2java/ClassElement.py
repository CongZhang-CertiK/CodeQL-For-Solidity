class ClassElement:
    def __init__(self):
        self.inherited_from = None
        self.class_name = ""
        self.type = ""
        self.indent = ""
        self.content_lines: list[str] = []

    def get_content(self):
        return self.class_name

    def get_signature(self):
        return ""
