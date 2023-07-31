package certik.congzhang.tool.codeql.solidity.builtins;

import java.math.BigInteger;

public class address {
    private BigInteger value;

    public address(BigInteger value) {
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {
            throw new IllegalArgumentException("Value is out of range for Address");
        }
        this.value = value;
    }

    public BigInteger value() {
        return value;
    }

    private static final BigInteger MAX_VALUE = new BigInteger("ffffffffffffffffffffffffffffffffffffffff", 16);

    public BigInteger balance() {
        return null;
    }

    public Boolean transfer(BigInteger amount) {
        return Boolean.FALSE;
    }

    public Boolean send(BigInteger amount) {
        return Boolean.FALSE;
    }

    public Boolean call(byte[] data) {
        return Boolean.FALSE;
    }

    public Boolean delegatecall(byte[] data) {
        return Boolean.FALSE;
    }

    public Boolean staticcall(byte[] data) {
        return Boolean.FALSE;
    }

    public Boolean equalTo(Object o) {
        return Boolean.FALSE;
    }

    public Boolean notEqualTo(Object o) {
        return Boolean.FALSE;
    }
}

