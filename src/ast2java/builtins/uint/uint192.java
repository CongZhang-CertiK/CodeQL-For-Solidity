
package builtins.uint;

import java.math.BigInteger;

public class uint192 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(192).subtract(BigInteger.ONE);

    public uint192(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint192(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint192(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
