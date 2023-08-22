
package builtins.uint;

import java.math.BigInteger;

public class uint144 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(144).subtract(BigInteger.ONE);

    public uint144(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint144(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint144(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
