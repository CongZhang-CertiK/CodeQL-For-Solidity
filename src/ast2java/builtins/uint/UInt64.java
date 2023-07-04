
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class UInt64 implements UInt {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(64).subtract(BigInteger.ONE);

    public UInt64(BigInteger value) {
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {
            throw new IllegalArgumentException("Value is out of range for UInt64");
        }
        this.value = value;
    }

    @Override
    public BigInteger value() {
        return value;
    }

    @Override
    public UInt add(UInt other) {
        return new UInt64(this.value().add(other.value()));
    }

    @Override
    public UInt subtract(UInt other) {
        return new UInt64(this.value().subtract(other.value()));
    }

    @Override
    public UInt multiply(UInt other) {
        return new UInt64(this.value().multiply(other.value()));
    }

    @Override
    public UInt divide(UInt other) {
        return new UInt64(this.value().divide(other.value()));
    }

    @Override
    public UInt mod(UInt other) {
        return new UInt64(this.value().mod(other.value()));
    }

    @Override
    public UInt pow(UInt exponent) {
        return new UInt64(this.value().pow(exponent.value().intValue()));
    }

    @Override
    public UInt and(UInt other) {
        return new UInt64(this.value().and(other.value()));
    }

    @Override
    public UInt or(UInt other) {
        return new UInt64(this.value().or(other.value()));
    }

    @Override
    public UInt xor(UInt other) {
        return new UInt64(this.value().xor(other.value()));
    }

    @Override
    public UInt not() {
        return new UInt64(this.value().not());
    }

    @Override
    public UInt shiftLeft(int n) {
        return new UInt64(this.value().shiftLeft(n));
    }

    @Override
    public UInt shiftRight(int n) {
        return new UInt64(this.value().shiftRight(n));
    }
}
