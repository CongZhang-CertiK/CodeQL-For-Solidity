package builtins;

public class string {

    public String value = "";

    public string(){

    }

    public string(Object o){
        value = o.toString();
    }

}
