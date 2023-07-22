
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint72 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(72).subtract(BigInteger.ONE);

    public uint72(BigInteger value) {
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {
            throw new IllegalArgumentException("Value is out of range for uint72");
        }
        this.value = value;
    }
    
    public uint72(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint72(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }

    @Override
    public uint add(uint other) {
        return new uint72(this.value().add(other.value()));
    }

    @Override
    public uint subtract(uint other) {
        return new uint72(this.value().subtract(other.value()));
    }

    @Override
    public uint multiply(uint other) {
        return new uint72(this.value().multiply(other.value()));
    }

    @Override
    public uint divide(uint other) {
        return new uint72(this.value().divide(other.value()));
    }

    @Override
    public uint mod(uint other) {
        return new uint72(this.value().mod(other.value()));
    }

    @Override
    public uint pow(uint exponent) {
        return new uint72(this.value().pow(exponent.value().intValue()));
    }

    @Override
    public uint and(uint other) {
        return new uint72(this.value().and(other.value()));
    }

    @Override
    public uint or(uint other) {
        return new uint72(this.value().or(other.value()));
    }

    @Override
    public uint xor(uint other) {
        return new uint72(this.value().xor(other.value()));
    }

    @Override
    public uint not() {
        return new uint72(this.value().not());
    }

    @Override
    public uint shiftLeft(int n) {
        return new uint72(this.value().shiftLeft(n));
    }

    @Override
    public uint shiftRight(int n) {
        return new uint72(this.value().shiftRight(n));
    }
}