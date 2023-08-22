package builtins;

import java.util.ArrayList;

public class Result {
    ArrayList<Object> result;
    public Result(Object... o){

    }

    public Object get(int i){
        return result.get(i);
    }
}
