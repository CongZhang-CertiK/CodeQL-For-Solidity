
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint96 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(96).subtract(BigInteger.ONE);

    public uint96(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint96(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint96(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
