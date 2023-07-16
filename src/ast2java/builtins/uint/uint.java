package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public interface uint {

  BigInteger value();

  uint add(uint other);

  uint subtract(uint other);

  uint multiply(uint other);

  uint divide(uint other);

  uint mod(uint other);

  uint pow(uint exponent);

  uint and(uint other);

  uint or(uint other);

  uint xor(uint other);

  uint not();

  uint shiftLeft(int n);

  uint shiftRight(int n);

}