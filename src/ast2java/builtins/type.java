package certik.congzhang.tool.codeql.solidity.builtins;

import certik.congzhang.tool.codeql.solidity.builtins.bytes.*;
import certik.congzhang.tool.codeql.solidity.builtins.uint.*;
import certik.congzhang.tool.codeql.solidity.builtins.string;

public class type {
    public bytes4 interfaceId = new bytes4();

    public bytes creationCode = new bytes();

    public bytes runtimeCode = new bytes();

    public string name = new string();

    public uint256 min = new uint256(0);

    public uint256 max = new uint256(1);

    public type(Class<?> clazz){
    }
}
