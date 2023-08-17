import os.path

from src.ast2java.definitions.ClassElement import ClassElement
from .FunctionDefinition import FunctionDefinition
from .EnumDefinition import EnumDefinition
from .StructDefinition import StructDefinition
from .EventDefinition import EventDefinition
from .ModifierDefinition import ModifierDefinition
from .StateVariableDeclaration import StateVariableDeclaration
from src.config import CONFIG
from src.logger import logger
from src.ast2java.utils import list_to_str


class JavaSourceFile:
    def __init__(self, compilation_global):
        self.compilation_global = compilation_global
        self.file_name = ""
        self.pragma_info = ""
        self.package_info = "package certik.congzhang.tool.codeql.solidity;"
        # methods implemented by this contract
        self.implements = {}
        self.class_type = ""
        self.class_name = ""
        self.eol = "\n\n"
        self.import_block: list[str] = []
        self.class_definition_start = ""
        self.class_definition_end = "\n}"
        self.class_elements: list[ClassElement] = []
        # functions in this contract
        self.functions = {}
        # fields in this contract
        self.declarations = {}
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
        self.class_definition_start = ""
        base_contracts = []
        if self.ast.get('baseContracts') is not None:
            for base_contract in self.ast.get('baseContracts'):
                base_contracts.append(base_contract.get('baseName').get('namePath'))
        self.class_definition_start += f"@inherit({{{list_to_str(base_contracts)}}})\n"
        self.class_definition_start += f"public {self.class_type} {self.class_name} {{"
        for name in base_contracts:
            contract: JavaSourceFile = self.compilation_global[name]
            self.update_class_elements(contract.class_elements, name)
        for subnode in ast.get('subNodes'):
            self.update_subnode(subnode)
        self.update_imports()

    def update_class_elements(self, class_elements, name):
        for class_element in class_elements:
            element_type = class_element.type
            if element_type == "FunctionDefinition":
                if len(class_element.body_ast) == 0:
                    self.implements[class_element.get_signature()] = name
                    continue
                if class_element.is_constructor:
                    class_element.java_modifiers += "private void "
            class_element.inherit_from = name
            class_element.parent = self
            index = self.has_same_element(class_element)
            if index is None:
                self.class_elements.append(class_element)

    def has_same_element(self, element):
        element_sig = element.get_signature()
        for index in range(0, len(self.class_elements)):
            if self.class_elements[index].get_signature() == element_sig:
                return index
        return None

    def element_override(self, element):
        element_sig = element.get_signature()
        index = self.has_same_element(element)
        if index is not None:
            self.class_elements.pop(index)
        if element_sig in self.implements.keys():
            element.implement = self.implements[element_sig]

    def update_subnode(self, subnode):
        node_type = subnode.get('type')
        if node_type == "FunctionDefinition":
            function_def = FunctionDefinition(subnode, self)
            self.element_override(function_def)
            self.class_elements.append(function_def)
            # TODO: 这里应该用函数签名作key，暂时跳过
            self.functions[function_def.name] = function_def
        elif node_type == "StateVariableDeclaration":
            state_var_decl = StateVariableDeclaration(subnode, self)
            self.element_override(state_var_decl)
            self.class_elements.append(state_var_decl)
            self.declarations.update(state_var_decl.var_decl_map)
        elif node_type == "EnumDefinition":
            enum_def = EnumDefinition(subnode, self)
            self.element_override(enum_def)
            self.class_elements.append(enum_def)
        elif node_type == "StructDefinition":
            struct_def = StructDefinition(subnode, self)
            self.element_override(struct_def)
            self.class_elements.append(struct_def)
        elif node_type == "EventDefinition":
            event_def = EventDefinition(subnode, self)
            self.element_override(event_def)
            self.class_elements.append(event_def)
        elif node_type == "UsingForDeclaration":
            pass
        elif node_type == "ModifierDefinition":
            modifier_def = ModifierDefinition(subnode, self)
            self.element_override(modifier_def)
            self.class_elements.append(modifier_def)
        else:
            logger.info(node_type)

    def update_imports(self):
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.modifiers.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.bytes.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.uint.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.storage.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.address;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.msg;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.string;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.inherit.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.hint.*;\n")
        self.import_block.append("import certik.congzhang.tool.codeql.solidity.builtins.functions.*;\n")
        self.import_block.append("import static certik.congzhang.tool.codeql.solidity.builtins.functions.sol.*;\n")
        self.import_block.append("import static certik.congzhang.tool.codeql.solidity.builtins.functions.asm.*;\n")
        self.import_block.append("\n")
        self.import_block.append("import java.util.Map;\n")
        self.import_block.append("import java.util.ArrayList;\n")

    def write_to_file(self):
        if not os.path.exists(CONFIG.dist):
            os.mkdir(CONFIG.dist)
        file = open(os.path.join(CONFIG.dist, self.file_name), "w")
        file.write(self.pragma_info)
        file.write("\n// Generated using [CodeQL-For-Solidity] by CertiK.com")
        file.write(self.eol)
        file.write(self.package_info)
        file.write(self.eol)
        for import_stmt in self.import_block:
            file.write(import_stmt)
        file.write(self.eol)
        file.write(self.class_definition_start)
        # file.write(self.eol)
        for class_element in self.class_elements:  # type: ClassElement
            file.write(self.eol)
            file.write(class_element.get_content())
        file.write(self.class_definition_end)
        file.close()
        logger.info(f"[GENERATED] {self.file_name}")
