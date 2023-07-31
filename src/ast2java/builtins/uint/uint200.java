
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint200 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(200).subtract(BigInteger.ONE);

    public uint200(Object o) {
        this.value = new BigInteger(String.valueOf(o));
    }
    
    public uint200(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint200(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }
}
