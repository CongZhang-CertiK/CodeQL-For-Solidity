import os

template = '''
package certik.congzhang.tool.codeql.solidity.builtins.bytes;

import java.math.BigInteger;

public class Bytes{n} implements IBytes {{
    private static final int SIZE = {n};
    private byte[] bytes = new byte[SIZE];

    public Bytes{n}() {{

    }}

    public Bytes{n}(int value) {{
        for (int i = 0; i < SIZE; i++) {{
            bytes[i] = (byte) ((value >> (8 * i)) & 0xFF);
        }}
    }}

    public Bytes{n}(String value) {{
        BigInteger bigInt = new BigInteger(value, 16);
        byte[] temp = bigInt.toByteArray();
        int len = temp.length;
        if (len > SIZE) {{
            throw new IllegalArgumentException("Input string is too long to fit into Bytes{n}");
        }}
        System.arraycopy(temp, 0, bytes, SIZE - len, len);
    }}

    @Override
    public int length() {{
        return SIZE;
    }}

    @Override
    public byte get(int index) {{
        return bytes[index];
    }}

    @Override
    public void set(int index, byte value) {{
        bytes[index] = value;
    }}

    @Override
    public byte[] toBytesN(int n) {{
        if (n != SIZE) {{
            throw new IllegalArgumentException("Cannot convert to a different bytesN type");
        }}
        return bytes.clone();
    }}

    @Override
    public void fromBytesN(byte[] bytesN) {{
        if (bytesN.length != SIZE) {{
            throw new IllegalArgumentException("Size of bytesN does not match N");
        }}
        System.arraycopy(bytesN, 0, bytes, 0, SIZE);
    }}
}}
'''

for i in range(1, 33):
    with open(os.path.join('./', f'Bytes{i}.java'), 'w') as f:
        f.write(template.format(n=i))
