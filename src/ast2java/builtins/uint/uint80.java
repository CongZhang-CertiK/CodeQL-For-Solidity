
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint80 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(80).subtract(BigInteger.ONE);

    public uint80(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint80(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint80(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
