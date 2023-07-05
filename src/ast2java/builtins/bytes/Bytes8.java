
package certik.congzhang.tool.codeql.solidity.builtins.bytes;

import java.math.BigInteger;

public class Bytes8 implements IBytes {
    private static final int SIZE = 8;
    private byte[] bytes = new byte[SIZE];

    public Bytes8() {

    }

    public Bytes8(int value) {
        for (int i = 0; i < SIZE; i++) {
            bytes[i] = (byte) ((value >> (8 * i)) & 0xFF);
        }
    }

    public Bytes8(String value) {
        BigInteger bigInt = new BigInteger(value, 16);
        byte[] temp = bigInt.toByteArray();
        int len = temp.length;
        if (len > SIZE) {
            throw new IllegalArgumentException("Input string is too long to fit into Bytes8");
        }
        System.arraycopy(temp, 0, bytes, SIZE - len, len);
    }

    @Override
    public int length() {
        return SIZE;
    }

    @Override
    public byte get(int index) {
        return bytes[index];
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
