
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint104 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(104).subtract(BigInteger.ONE);

    public uint104(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint104(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint104(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
