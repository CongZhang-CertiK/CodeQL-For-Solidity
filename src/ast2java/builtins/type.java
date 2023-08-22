package builtins;

import builtins.bytes.*;
import builtins.uint.*;
import builtins.string;

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
