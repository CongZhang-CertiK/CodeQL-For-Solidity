
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint40 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(40).subtract(BigInteger.ONE);

    public uint40(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint40(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint40(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
