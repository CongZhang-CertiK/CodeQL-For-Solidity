
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint88 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(88).subtract(BigInteger.ONE);

    public uint88(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint88(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint88(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
