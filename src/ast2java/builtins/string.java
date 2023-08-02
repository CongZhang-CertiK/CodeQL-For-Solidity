package certik.congzhang.tool.codeql.solidity.builtins;

public class string {

    public String value = "";

    public string(){

    }

    public string(Object o){
        value = o.toString();
    }

}
