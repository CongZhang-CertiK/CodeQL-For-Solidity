
package builtins.uint;

import java.math.BigInteger;

public class uint240 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(240).subtract(BigInteger.ONE);

    public uint240(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint240(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint240(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
