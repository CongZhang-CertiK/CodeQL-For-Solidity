
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint176 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(176).subtract(BigInteger.ONE);

    public uint176(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint176(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint176(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
