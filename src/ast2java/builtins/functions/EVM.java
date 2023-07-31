package certik.congzhang.tool.codeql.solidity.builtins.functions;

public class EVM {
    public static void require(Object... o){}

    public static void revert(Object... o){}

    public static <T> T _add(T o1, T o2){ return o1;}

    public static <T> T _sub(T o1, T o2){ return o1;}

    public static <T> T _mul(T o1, T o2){ return o1;}

    public static <T> T _div(T o1, T o2){ return o1;}

    public static <T> T _mod(T o1, T o2){ return o1;}

    public static <T> T _pow(T o1, T o2){ return o1;}

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

    public static void _rightShiftAssign(Object o1, Object o2){}

    public static void _leftShiftAssign(Object o1, Object o2){}

}
