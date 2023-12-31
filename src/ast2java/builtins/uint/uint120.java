
package builtins.uint;

import java.math.BigInteger;

public class uint120 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(120).subtract(BigInteger.ONE);

    public uint120(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint120(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint120(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
