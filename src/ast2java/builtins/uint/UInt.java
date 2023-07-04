package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public interface UInt {
    BigInteger value();

    UInt add(UInt other);
    UInt subtract(UInt other);
    UInt multiply(UInt other);
    UInt divide(UInt other);
    UInt mod(UInt other);
    UInt pow(UInt exponent);
    UInt and(UInt other);
    UInt or(UInt other);
    UInt xor(UInt other);
    UInt not();
    UInt shiftLeft(int n);
    UInt shiftRight(int n);
}