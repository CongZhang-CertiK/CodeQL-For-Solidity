
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint64 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(64).subtract(BigInteger.ONE);

    public uint64(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint64(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint64(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
