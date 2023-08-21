package certik.congzhang.tool.codeql.solidity.builtins;

import certik.congzhang.tool.codeql.solidity.builtins.uint.uint256;

import java.util.ArrayList;

public class array<T> extends ArrayList<T> {
    public uint256 length;
    public boolean push(T t) {
        return super.add(t);
    }

    public T get(uint256 i) {
        return super.get(i.value().intValue());
    }
}
