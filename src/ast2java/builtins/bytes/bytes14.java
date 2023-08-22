
package builtins.bytes;

import builtins.uint.uint;
import builtins.uint.uint256;

import java.math.BigInteger;

public class bytes14 implements Ibytes {
    private static final int SIZE = 14;
    private byte[] bytes = new byte[SIZE];
    public uint256 length;

    public bytes14() {

    }

    public bytes14(Object o) {

    }

    @Override
    public int length() {
        return SIZE;
    }

    @Override
    public byte get(int index) {
        return bytes[index];
    }
    
    public byte get(uint o) {
        return bytes[o.value().intValue()];
    }

    @Override
    public void set(int index, byte value) {
        bytes[index] = value;
    }

    @Override
    public byte[] toBytesN(int n) {
        if (n != SIZE) {
            throw new IllegalArgumentException("Cannot convert to a different bytesN type");
        }
        return bytes.clone();
    }

    @Override
    public void fromBytesN(byte[] bytesN) {
        if (bytesN.length != SIZE) {
            throw new IllegalArgumentException("Size of bytesN does not match N");
        }
        System.arraycopy(bytesN, 0, bytes, 0, SIZE);
    }
}
