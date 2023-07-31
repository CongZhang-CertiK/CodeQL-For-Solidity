
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint120 implements uint {
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow(120).subtract(BigInteger.ONE);

    public uint120(BigInteger value) {
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {
            throw new IllegalArgumentException("Value is out of range for uint120");
        }
        this.value = value;
    }
    
    public uint120(int value) {
        this(BigInteger.valueOf(value));
    }

    public uint120(long value) {
        this(BigInteger.valueOf(value));
    }

    @Override
    public BigInteger value() {
        return value;
    }

    @Override
    public uint _add(uint other) {
        return new uint120(this.value().add(other.value()));
    }

    @Override
    public uint _sub(uint other) {
        return new uint120(this.value().subtract(other.value()));
    }

    @Override
    public uint _mul(uint other) {
        return new uint120(this.value().multiply(other.value()));
    }

    @Override
    public uint _div(uint other) {
        return new uint120(this.value().divide(other.value()));
    }

    @Override
    public uint _mod(uint other) {
        return new uint120(this.value().mod(other.value()));
    }

    @Override
    public uint _pow(uint exponent) {
        return new uint120(this.value().pow(exponent.value().intValue()));
    }
    
    @Override
    public Boolean _equal(uint other) {
        return Boolean.False;
    }

    @Override
    public uint _notEqual(uint other) {
        return Boolean.False;
    }

    @Override
    public Boolean _greaterEqual(uint other) {
        return Boolean.False;
    }

    @Override
    public uint _greaterThan(uint other) {
        return Boolean.False;
    }

    @Override
    public Boolean _lessEqual(uint other) {
        return Boolean.False;
    }

    @Override
    public uint _lessThan(uint other) {
        return Boolean.False;
    }
    
    @Override
    public void _assign(uint other) {
        this.value = other.value;
    }

    @Override
    public void _addAssign(uint other) {
        this.value += other.value;
    }

    @Override
    public void _subAssign(uint other) {
        this.value -= other.value;
    }

    @Override
    public uint and(uint other) {
        return new uint120(this.value().and(other.value()));
    }

    @Override
    public uint or(uint other) {
        return new uint120(this.value().or(other.value()));
    }

    @Override
    public uint xor(uint other) {
        return new uint120(this.value().xor(other.value()));
    }

    @Override
    public uint not() {
        return new uint120(this.value().not());
    }

    @Override
    public uint shiftLeft(int n) {
        return new uint120(this.value().shiftLeft(n));
    }

    @Override
    public uint shiftRight(int n) {
        return new uint120(this.value().shiftRight(n));
    }
}
