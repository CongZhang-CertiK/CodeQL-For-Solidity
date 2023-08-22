
package builtins.uint;

import java.math.BigInteger;

public class uint8 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(8).subtract(BigInteger.ONE);

    public uint8(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint8(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint8(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
