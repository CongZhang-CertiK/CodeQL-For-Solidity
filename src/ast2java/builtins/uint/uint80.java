
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint80 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(80).subtract(BigInteger.ONE);

    public uint80(BigInteger value) {
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {
            throw new IllegalArgumentException("Value is out of range for uint80");
        }
        this.value = value;
    }
    
    public uint80(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint80(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }

    @Override
    public uint add(uint other) {
        return new uint80(this.value().add(other.value()));
    }

    @Override
    public uint subtract(uint other) {
        return new uint80(this.value().subtract(other.value()));
    }

    @Override
    public uint multiply(uint other) {
        return new uint80(this.value().multiply(other.value()));
    }

    @Override
    public uint divide(uint other) {
        return new uint80(this.value().divide(other.value()));
    }

    @Override
    public uint mod(uint other) {
        return new uint80(this.value().mod(other.value()));
    }

    @Override
    public uint pow(uint exponent) {
        return new uint80(this.value().pow(exponent.value().intValue()));
    }

    @Override
    public uint and(uint other) {
        return new uint80(this.value().and(other.value()));
    }

    @Override
    public uint or(uint other) {
        return new uint80(this.value().or(other.value()));
    }

    @Override
    public uint xor(uint other) {
        return new uint80(this.value().xor(other.value()));
    }

    @Override
    public uint not() {
        return new uint80(this.value().not());
    }

    @Override
    public uint shiftLeft(int n) {
        return new uint80(this.value().shiftLeft(n));
    }

    @Override
    public uint shiftRight(int n) {
        return new uint80(this.value().shiftRight(n));
    }
}
