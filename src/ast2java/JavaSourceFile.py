import os.path

from .ClassElement import ClassElement
from .FunctionDefinition import FunctionDefinition
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
        self.compilation_unit = None

    def keywork_mapping(self, word):
        mapping = {
            'contract': 'class',
            'interface': 'interface',
            'library': 'class',
            'abstract': 'interface'
        }
        return mapping[word]

    def update(self, cu):
        self.file_name = cu.get('name') + ".java"
        self.class_name = cu.get('name')
        self.class_type = self.keywork_mapping(cu.get('kind'))
        self.class_definition_start = f"public {self.class_type} {self.class_name} {{"
        for subnode in cu.get('subNodes'):
            node_type = subnode.get('type')
            if node_type == "FunctionDefinition":
                self.class_elements.append(FunctionDefinition(subnode, self.class_type))
            else:
                pass
        self.update_imports()

    def update_imports(self):
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.*;")

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
