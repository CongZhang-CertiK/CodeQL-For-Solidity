
package builtins.uint;

import java.math.BigInteger;

public class uint256 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(256).subtract(BigInteger.ONE);

    public uint256(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint256(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint256(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
