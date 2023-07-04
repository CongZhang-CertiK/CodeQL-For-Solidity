package certik.congzhang.tool.codeql.solidity.builtins.bytes;

public interface IBytes {
    int length();
    byte get(int index);
    void set(int index, byte value);
    byte[] toBytesN(int n);
    void fromBytesN(byte[] bytesN);
}

