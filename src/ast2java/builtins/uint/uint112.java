
package builtins.uint;

import java.math.BigInteger;

public class uint112 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(112).subtract(BigInteger.ONE);

    public uint112(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint112(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint112(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
