package builtins.functions;

import builtins.string;
import builtins.uint.uint256;

public class asm {

    public static <T> T add(T o1, T o2){ return o1;}

    public static <T> T add(T o1, Boolean o2){ return o1;}

    public static <T> T add(Boolean o1, T o2){ return o2;}

    public static <T> T add(T o1, string o2){return o1;}

    public static <T> T add(string o1, T o2){return o2;}

    public static <T> T sub(T o1, T o2){ return o1;}

    public static <T> T sub(T o1, Boolean o2){ return o1;}

    public static <T> T sub(Boolean o1, T o2){ return o2;}

    public static <T> T sub(T o1, string o2){return o1;}

    public static <T> T sub(string o1, T o2){return o2;}

    public static <T> T mul(T o1, T o2){ return o1;}

    public static <T> T mul(T o1, Boolean o2){ return o1;}

    public static <T> T div(T o1, T o2){ return o1;}

    public static <T> T div(T o1, Boolean o2){ return o1;}

    public static <T> T mod(T o1, T o2){ return o1;}

    public static <T> T mod(T o1, Boolean o2){ return o1;}

    public static <T> T pow(T o1, T o2){ return o1;}

    public static <T> T pow(T o1, Boolean o2){ return o1;}

    public static <T> T and(T o1, T o2){ return o1;}

    public static <T> T and(T o1, Boolean o2){ return o1;}

    public static <T> T or(T o1, T o2){ return o1;}

    public static <T> T or(T o1, Boolean o2){ return o1;}

    public static <T> T xor(T o1, T o2){ return o1;}

    public static <T> T xor(T o1, Boolean o2){ return o1;}

    public static <T> T not(T o1){ return o1; }

    public static Boolean eq(Object o1, Object o2){ return o1 == o2; }

    public static Boolean neq(Object o1, Object o2){ return o1 == o2; }

    public static Boolean gt(Object o1, Object o2){ return o1 == o2; }

    public static Boolean geq(Object o1, Object o2){ return o1 == o2; }

    public static Boolean lt(Object o1, Object o2){ return o1 == o2; }

    public static Boolean leq(Object o1, Object o2){ return o1 == o2; }

}
