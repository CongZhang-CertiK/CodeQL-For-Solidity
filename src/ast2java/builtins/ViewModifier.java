package certik.congzhang.tool.codeql.solidity.builtins;

import java.lang.annotation.*;

@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
public @interface ViewModifier {
    String value() default "view";
}
