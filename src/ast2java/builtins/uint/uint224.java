
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint224 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(224).subtract(BigInteger.ONE);

    public uint224(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint224(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint224(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
