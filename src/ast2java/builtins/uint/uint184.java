
package builtins.uint;

import java.math.BigInteger;

public class uint184 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(184).subtract(BigInteger.ONE);

    public uint184(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint184(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint184(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
