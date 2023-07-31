
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint136 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(136).subtract(BigInteger.ONE);

    public uint136(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint136(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint136(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
