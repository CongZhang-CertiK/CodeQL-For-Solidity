package certik.congzhang.tool.codeql.solidity.builtins.bytes;

public class Bytes18 implements IBytes {
    private int n = 18;
    private byte[] bytes = new byte[18];

    public Bytes18() {

    }

    @Override
    public int length() {
        return n;
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
        if (n != this.n) {
            throw new IllegalArgumentException("Cannot convert to a different bytesN type");
        }
        return bytes.clone();
    }

    @Override
    public void fromBytesN(byte[] bytesN) {
        if (bytesN.length != n) {
            throw new IllegalArgumentException("Size of bytesN does not match N");
        }
        System.arraycopy(bytesN, 0, bytes, 0, n);
    }
}
