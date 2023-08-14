from src.ast2java.definitions.ClassElement import ClassElement
from src.logger import logger
from src.ast2java.statements.Block import Block


class ModifierDefinition(ClassElement):
    def __init__(self, ast, parent):
        super().__init__()
        self.ast = ast
        self.parent = parent
        self.eol = "\n\t"
        self.name = self.ast.get('name')
        self.body = Block(self.ast.get('body'), self, self.eol).get_content()
        parent.import_block.append("import java.lang.annotation.ElementType;\n")
        parent.import_block.append("import java.lang.annotation.Retention;\n")
        parent.import_block.append("import java.lang.annotation.RetentionPolicy;\n")
        parent.import_block.append("import java.lang.annotation.Target;\n")

    def get_signature(self):
        return str(self.body)

    def get_content(self):
        result = super().get_content()
        result += f"{self.eol}@Target({{ElementType.METHOD, ElementType.CONSTRUCTOR}})"
        result += f"{self.eol}@Retention(RetentionPolicy.RUNTIME)"
        result += f"{self.eol}public @interface {self.name} {{}}"
        result += f"{self.eol}public void {self.name}()"
        result += self.body
        return result
