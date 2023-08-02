package certik.congzhang.tool.codeql.solidity.builtins;

import java.math.BigInteger;

public class address {
    private BigInteger value;

    public address(Object o){
        this.value = new BigInteger(o.toString());
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

