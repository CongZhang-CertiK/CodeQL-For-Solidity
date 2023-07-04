package certik.congzhang.tool.codeql.solidity.builtins;

import java.math.BigInteger;

public class Address {
    private BigInteger value;

    public Address(BigInteger value) {
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {
            throw new IllegalArgumentException("Value is out of range for Address");
        }
        this.value = value;
    }

    public BigInteger value() {
        return value;
    }

    private static final BigInteger MAX_VALUE = new BigInteger("ffffffffffffffffffffffffffffffffffffffff", 16);

    // 声明balance方法
    public BigInteger balance() {
        // 暂不实现，返回null
        return null;
    }

    // 声明transfer方法
    public boolean transfer(BigInteger amount) {
        // 暂不实现，返回false
        return false;
    }

    // 声明send方法
    public boolean send(BigInteger amount) {
        // 暂不实现，返回false
        return false;
    }

    // 声明call方法
    public boolean call(byte[] data) {
        // 暂不实现，返回false
        return false;
    }

    // 声明delegatecall方法
    public boolean delegatecall(byte[] data) {
        // 暂不实现，返回false
        return false;
    }

    // 声明staticcall方法
    public boolean staticcall(byte[] data) {
        // 暂不实现，返回false
        return false;
    }
}

