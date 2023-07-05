import os.path

from .ClassElement import ClassElement
from .FunctionDefinition import FunctionDefinition
from .StateVariableDeclaration import StateVariableDeclaration
from src.config import CONFIG
from src.logger import logger


class JavaSourceFile:
    def __init__(self):
        self.file_name = ""
        self.pragma_info = ""
        self.package_info = "package certik.congzhang.tool.codeql.solidity;"
        self.class_type = ""
        self.class_name = ""
        self.eol = "\n\n"
        self.import_block: list[str] = []
        self.class_definition_start = ""
        self.class_definition_end = "\n}"
        self.class_elements: list[ClassElement] = []
        self.ast = None

    def keywork_mapping(self, word):
        mapping = {
            'contract': 'class',
            'interface': 'interface',
            'library': 'class',
            'abstract': 'abstract class'
        }
        return mapping[word]

    def update(self, ast):
        self.file_name = ast.get('name') + ".java"
        self.class_name = ast.get('name')
        self.class_type = self.keywork_mapping(ast.get('kind'))
        self.class_definition_start = f"public {self.class_type} {self.class_name} {{"
        for subnode in ast.get('subNodes'):
            node_type = subnode.get('type')
            if node_type == "FunctionDefinition":
                self.class_elements.append(FunctionDefinition(subnode, self))
            elif node_type == "StateVariableDeclaration":
                self.class_elements.append(StateVariableDeclaration(subnode))
            elif node_type == "EnumDefinition":
                pass
            elif node_type == "StructDefinition":
                pass
            elif node_type == "EventDefinition":
                pass
            elif node_type == "UsingForDeclaration":
                pass
            elif node_type == "ModifierDefinition":
                pass
            else:
                logger.info(node_type)
        self.update_imports()

    def update_imports(self):
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.modifiers.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.bytes.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.uint.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.Address;\n")

    def write_to_file(self):
        if not os.path.exists(CONFIG.dist):
            os.mkdir(CONFIG.dist)
        file = open(os.path.join(CONFIG.dist, self.file_name), "w")
        file.write(self.pragma_info)
        file.write(self.eol)
        file.write(self.package_info)
        file.write(self.eol)
        for import_stmt in self.import_block:
            file.write(import_stmt)
        file.write(self.eol)
        file.write(self.class_definition_start)
        file.write(self.eol)
        for class_element in self.class_elements:  # type: ClassElement
            file.write(class_element.get_content())
        file.write(self.class_definition_end)
        file.close()
