class ClassElement:
    def __init__(self):
        self.inherit_from = None
        self.override_from = None
        self.parent = None
        self.eol = "\n\t"
        self.name = ""
        self.type = ""

    def get_content(self):
        result = ""
        if self.inherit_from is not None:
            result += f"{self.eol}@inherit(\"{self.inherit_from}\")"
        if self.override_from is not None:
            result += f"{self.eol}@override(\"{self.override_from}\")"
        return result

    def get_signature(self):
        return ""
