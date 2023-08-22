package builtins.bytes;

public interface Ibytes {
    int length();
    byte get(int index);
    void set(int index, byte value);
    byte[] toBytesN(int n);
    void fromBytesN(byte[] bytesN);
}

