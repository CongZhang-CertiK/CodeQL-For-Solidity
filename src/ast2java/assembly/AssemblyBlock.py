from src.logger import logger


class AssemblyBlock:
    def __init__(self, _ast, eol):
        self.ast = _ast
        self.eol = eol

    def get_content(self):
        if self.ast.get('type') == "AssemblyBlock":
            result = "{"
            for statement in self.ast.get('operations'):
                result = self.update_by_operation(statement, result)
            result += self.eol + "}"
        else:
            result = self.update_by_operation(self.ast, "")
        return result

    def update_by_operation(self, operation, result):
        op = None
        if operation.get('type') == "AssemblyLocalDefinition":
            from src.ast2java.assembly.AssemblyLocalDefinition import AssemblyLocalDefinition
            op = AssemblyLocalDefinition(operation, self.eol + "\t")
        elif operation.get('type') == "AssemblyAssignment":
            from src.ast2java.assembly.AssemblyAssignment import AssemblyAssignment
            op = AssemblyAssignment(operation, self.eol + "\t")
        else:
            logger.debug("unresolved assembly statement: " + operation.get('type'))
        if op is not None:
            result += op.get_content()
        return result
