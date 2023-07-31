
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint152 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(152).subtract(BigInteger.ONE);

    public uint152(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint152(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint152(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
