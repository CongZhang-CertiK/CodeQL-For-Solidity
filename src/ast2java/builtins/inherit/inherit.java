package builtins.inherit;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.CONSTRUCTOR, ElementType.TYPE, ElementType.FIELD, ElementType.METHOD})
public @interface inherit {
    String[] value() default {};
}
