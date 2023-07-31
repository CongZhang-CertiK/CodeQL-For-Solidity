
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint56 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(56).subtract(BigInteger.ONE);

    public uint56(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint56(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint56(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
