package certik.congzhang.tool.codeql.solidity.builtins.hint;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.METHOD})
public @interface error {
    String[] value() default {};
}
