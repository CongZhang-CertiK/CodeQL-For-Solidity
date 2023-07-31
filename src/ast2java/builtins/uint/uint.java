package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public interface uint {

  BigInteger value();

  uint _add(uint other);

  uint _sub(uint other);

  uint _mul(uint other);

  uint _div(uint other);

  uint _mod(uint other);

  uint _pow(uint exponent);

  uint _equal(uint other);

  uint _notEqual(uint other);

  uint _greaterThan(uint other);

  uint _greaterEqual(uint other);

  uint _lessThan(uint other);

  uint _lessEqual(uint other);

  uint _assign(uint other);

  uint _subAssign(uint other);

  uint _addAssign(uint other);

  uint and(uint other);

  uint or(uint other);

  uint xor(uint other);

  uint not();

  uint shiftLeft(int n);

  uint shiftRight(int n);

}