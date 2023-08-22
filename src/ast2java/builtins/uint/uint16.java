
package builtins.uint;

import java.math.BigInteger;

public class uint16 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(16).subtract(BigInteger.ONE);

    public uint16(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint16(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint16(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
