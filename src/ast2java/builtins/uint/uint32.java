
package builtins.uint;

import java.math.BigInteger;

public class uint32 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(32).subtract(BigInteger.ONE);

    public uint32(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint32(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint32(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
