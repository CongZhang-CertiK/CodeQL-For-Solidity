
package builtins.uint;

import java.math.BigInteger;

public class uint160 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(160).subtract(BigInteger.ONE);

    public uint160(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint160(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint160(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
