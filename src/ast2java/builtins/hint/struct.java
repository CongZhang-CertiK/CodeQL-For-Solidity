package builtins.hint;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE})
public @interface struct {
    String[] value() default {};
}
