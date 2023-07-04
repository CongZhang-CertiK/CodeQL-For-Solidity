class ClassElement:
    def __init__(self):
        self.class_name = ""
        self.type = ""
        self.indent = ""
        self.content_lines: list[str] = []

    def get_content(self):
        return self.class_name
