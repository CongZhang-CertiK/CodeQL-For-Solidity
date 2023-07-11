
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint32 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(32).subtract(BigInteger.ONE);

    public uint32(BigInteger value) {
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {
            throw new IllegalArgumentException("Value is out of range for uint32");
        }
        this.value = value;
    }
    
    public uint32(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint32(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }

    @Override
    public uint add(uint other) {
        return new uint32(this.value().add(other.value()));
    }

    @Override
    public uint subtract(uint other) {
        return new uint32(this.value().subtract(other.value()));
    }

    @Override
    public uint multiply(uint other) {
        return new uint32(this.value().multiply(other.value()));
    }

    @Override
    public uint divide(uint other) {
        return new uint32(this.value().divide(other.value()));
    }

    @Override
    public uint mod(uint other) {
        return new uint32(this.value().mod(other.value()));
    }

    @Override
    public uint pow(uint exponent) {
        return new uint32(this.value().pow(exponent.value().intValue()));
    }

    @Override
    public uint and(uint other) {
        return new uint32(this.value().and(other.value()));
    }

    @Override
    public uint or(uint other) {
        return new uint32(this.value().or(other.value()));
    }

    @Override
    public uint xor(uint other) {
        return new uint32(this.value().xor(other.value()));
    }

    @Override
    public uint not() {
        return new uint32(this.value().not());
    }

    @Override
    public uint shiftLeft(int n) {
        return new uint32(this.value().shiftLeft(n));
    }

    @Override
    public uint shiftRight(int n) {
        return new uint32(this.value().shiftRight(n));
    }
}
