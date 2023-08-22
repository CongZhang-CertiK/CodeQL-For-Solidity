
package builtins.uint;

import java.math.BigInteger;

public class uint48 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(48).subtract(BigInteger.ONE);

    public uint48(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint48(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint48(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
