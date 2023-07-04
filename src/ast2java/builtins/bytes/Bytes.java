package certik.congzhang.tool.codeql.solidity.builtins.bytes;

import java.util.ArrayList;

public class Bytes implements IBytes {
    private ArrayList<Byte> bytes;

    public Bytes() {
        this.bytes = new ArrayList<>();
    }

    @Override
    public int length() {
        return bytes.size();
    }

    @Override
    public byte get(int index) {
        return bytes.get(index);
    }

    @Override
    public void set(int index, byte value) {
        bytes.set(index, value);
    }

    public void push(byte value) {
        bytes.add(value);
    }

    @Override
    public byte[] toBytesN(int n) {
        if (n > bytes.size()) {
            throw new IllegalArgumentException("N is greater than the length of this bytes array");
        }

        byte[] bytesN = new byte[n];
        for (int i = 0; i < n; i++) {
            bytesN[i] = bytes.get(i);
        }
        return bytesN;
    }

    @Override
    public void fromBytesN(byte[] bytesN) {
        bytes.clear();
        for (byte b : bytesN) {
            bytes.add(b);
        }
    }
}
