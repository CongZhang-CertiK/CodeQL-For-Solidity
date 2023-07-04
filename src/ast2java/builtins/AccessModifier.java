package certik.congzhang.tool.codeql.solidity.builtins;

import java.lang.annotation.*;

@Target({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD, ElementType.CONSTRUCTOR})
@Retention(RetentionPolicy.RUNTIME)
public @interface AccessModifier {
    String value() default "public";
}
