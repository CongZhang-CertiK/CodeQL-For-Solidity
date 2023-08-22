package certik.congzhang.tool.codeql.solidity.builtins.functions;

import certik.congzhang.tool.codeql.solidity.builtins.type;
import certik.congzhang.tool.codeql.solidity.builtins.uint.*;
import certik.congzhang.tool.codeql.solidity.builtins.bytes.*;
import certik.congzhang.tool.codeql.solidity.builtins.string;
import certik.congzhang.tool.codeql.solidity.builtins.address;

public class sol {
    public static void _require(Object... o){}

    public static void _revert(Object... o){}

    public static bytes32 _keccak256(Object... o){ return null; }

    public static address _ecrecover(Object... o){ return null; }

    public static void _unchecked_start(){}

    public static void _assembly_start(){}

    public static void _function_body(){}

    public static address payable(Object o){return new address(0);}

    public static <T> T _add(T o1, T o2){ return o1;}

    public static <T> T _sub(T o1, T o2){ return o1;}

    public static <T> T _mul(T o1, T o2){ return o1;}

    public static <T> T _div(T o1, T o2){ return o1;}

    public static <T> T _mod(T o1, T o2){ return o1;}

    public static <T> T _pow(T o1, T o2){ return o1;}

    public static <T> T _and(T o1, T o2){ return o1;}

    public static <T> T _or(T o1, T o2){ return o1;}

    public static <T> T _xor(T o1, T o2){ return o1;}

    public static <T> T _not(T o1){ return o1; }

    public static <T> T _increment(T o1){ return o1; }

    public static <T> T _decrement(T o1){ return o1; }

    public static <T> T _rightShift(T o1, T o2){ return o1;}

    public static <T> T _leftShift(T o1, T o2){ return o1;}

    public static Boolean _equal(Object o1, Object o2){ return o1 == o2; }

    public static Boolean _notEqual(Object o1, Object o2){ return o1 == o2; }

    public static Boolean _greaterThan(Object o1, Object o2){ return o1 == o2; }

    public static Boolean _greaterEqual(Object o1, Object o2){ return o1 == o2; }

    public static Boolean _lessThan(Object o1, Object o2){ return o1 == o2; }

    public static Boolean _lessEqual(Object o1, Object o2){ return o1 == o2; }

    public static void _assign(Object... o){}

    public static void _subAssign(Object o1, Object o2){}

    public static void _addAssign(Object o1, Object o2){}

    public static void _mulAssign(Object o1, Object o2){}

    public static void _divAssign(Object o1, Object o2){}

    public static void _modAssign(Object o1, Object o2){}

    public static void _andAssign(Object o1, Object o2){}

    public static void _orAssign(Object o1, Object o2){}

    public static void _xorAssign(Object o1, Object o2){}

    public static void _rightShiftAssign(Object o1, Object o2){}

    public static void _leftShiftAssign(Object o1, Object o2){}

    public static <T> T addmod(T x, T y, T k){ return x; }

    public static <T> T mulmod(T x, T y, T k){ return x; }

    public static string _string(Object o){ return new string(o); }

    public static address _address(Object o){ return new address(o); }

    public static Boolean _Boolean(Object o){ return Boolean.FALSE; }

    public static type _type(Class<?> clazz){ return new type(clazz); }

    public static uint256 _uint(Object i){ return new uint256(i); }
    public static uint8 _uint8(Object i) { return new uint8(i); }
    public static uint16 _uint16(Object i) { return new uint16(i); }
    public static uint24 _uint24(Object i) { return new uint24(i); }
    public static uint32 _uint32(Object i) { return new uint32(i); }
    public static uint40 _uint40(Object i) { return new uint40(i); }
    public static uint48 _uint48(Object i) { return new uint48(i); }
    public static uint56 _uint56(Object i) { return new uint56(i); }
    public static uint64 _uint64(Object i) { return new uint64(i); }
    public static uint72 _uint72(Object i) { return new uint72(i); }
    public static uint80 _uint80(Object i) { return new uint80(i); }
    public static uint88 _uint88(Object i) { return new uint88(i); }
    public static uint96 _uint96(Object i) { return new uint96(i); }
    public static uint104 _uint104(Object i) { return new uint104(i); }
    public static uint112 _uint112(Object i) { return new uint112(i); }
    public static uint120 _uint120(Object i) { return new uint120(i); }
    public static uint128 _uint128(Object i) { return new uint128(i); }
    public static uint136 _uint136(Object i) { return new uint136(i); }
    public static uint144 _uint144(Object i) { return new uint144(i); }
    public static uint152 _uint152(Object i) { return new uint152(i); }
    public static uint160 _uint160(Object i) { return new uint160(i); }
    public static uint168 _uint168(Object i) { return new uint168(i); }
    public static uint176 _uint176(Object i) { return new uint176(i); }
    public static uint184 _uint184(Object i) { return new uint184(i); }
    public static uint192 _uint192(Object i) { return new uint192(i); }
    public static uint200 _uint200(Object i) { return new uint200(i); }
    public static uint208 _uint208(Object i) { return new uint208(i); }
    public static uint216 _uint216(Object i) { return new uint216(i); }
    public static uint224 _uint224(Object i) { return new uint224(i); }
    public static uint232 _uint232(Object i) { return new uint232(i); }
    public static uint240 _uint240(Object i) { return new uint240(i); }
    public static uint248 _uint248(Object i) { return new uint248(i); }
    public static uint256 _uint256(Object i) { return new uint256(i); }

    public static bytes _bytes(Object i) { return new bytes(i); }
    public static bytes1 _bytes1(Object i) { return new bytes1(i); }
    public static bytes2 _bytes2(Object i) { return new bytes2(i); }
    public static bytes3 _bytes3(Object i) { return new bytes3(i); }
    public static bytes4 _bytes4(Object i) { return new bytes4(i); }
    public static bytes5 _bytes5(Object i) { return new bytes5(i); }
    public static bytes6 _bytes6(Object i) { return new bytes6(i); }
    public static bytes7 _bytes7(Object i) { return new bytes7(i); }
    public static bytes8 _bytes8(Object i) { return new bytes8(i); }
    public static bytes9 _bytes9(Object i) { return new bytes9(i); }
    public static bytes10 _bytes10(Object i) { return new bytes10(i); }
    public static bytes11 _bytes11(Object i) { return new bytes11(i); }
    public static bytes12 _bytes12(Object i) { return new bytes12(i); }
    public static bytes13 _bytes13(Object i) { return new bytes13(i); }
    public static bytes14 _bytes14(Object i) { return new bytes14(i); }
    public static bytes15 _bytes15(Object i) { return new bytes15(i); }
    public static bytes16 _bytes16(Object i) { return new bytes16(i); }
    public static bytes17 _bytes17(Object i) { return new bytes17(i); }
    public static bytes18 _bytes18(Object i) { return new bytes18(i); }
    public static bytes19 _bytes19(Object i) { return new bytes19(i); }
    public static bytes20 _bytes20(Object i) { return new bytes20(i); }
    public static bytes21 _bytes21(Object i) { return new bytes21(i); }
    public static bytes22 _bytes22(Object i) { return new bytes22(i); }
    public static bytes23 _bytes23(Object i) { return new bytes23(i); }
    public static bytes24 _bytes24(Object i) { return new bytes24(i); }
    public static bytes25 _bytes25(Object i) { return new bytes25(i); }
    public static bytes26 _bytes26(Object i) { return new bytes26(i); }
    public static bytes27 _bytes27(Object i) { return new bytes27(i); }
    public static bytes28 _bytes28(Object i) { return new bytes28(i); }
    public static bytes29 _bytes29(Object i) { return new bytes29(i); }
    public static bytes30 _bytes30(Object i) { return new bytes30(i); }
    public static bytes31 _bytes31(Object i) { return new bytes31(i); }
    public static bytes32 _bytes32(Object i) { return new bytes32(i); }
}
