
package builtins.uint;

import java.math.BigInteger;

public class uint232 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(232).subtract(BigInteger.ONE);

    public uint232(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint232(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint232(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
