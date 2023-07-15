package certik.congzhang.tool.codeql.solidity.builtins.inherit;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.FIELD, ElementType.METHOD})
public @interface implement {
    String[] value() default {};
}
