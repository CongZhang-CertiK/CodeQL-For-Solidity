
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint248 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(248).subtract(BigInteger.ONE);

    public uint248(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint248(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint248(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
