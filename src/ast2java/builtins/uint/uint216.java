
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint216 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(216).subtract(BigInteger.ONE);

    public uint216(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint216(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint216(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
