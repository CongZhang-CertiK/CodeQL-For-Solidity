package certik.congzhang.tool.codeql.solidity.builtins.functions;

import certik.congzhang.tool.codeql.solidity.builtins.uint.uint256;

public class EVM {
    public static void _require(Object... o){}

    public static void _revert(Object... o){}

    public static void _unchecked_start(){}

    public static uint256 _int(Object i){ return new uint256(i); }

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

    public static void _assign(Object o1, Object o2){}

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

}
