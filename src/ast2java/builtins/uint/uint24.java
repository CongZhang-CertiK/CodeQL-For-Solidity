
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint24 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(24).subtract(BigInteger.ONE);

    public uint24(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint24(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint24(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
