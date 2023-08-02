import os

template = '''
package certik.congzhang.tool.codeql.solidity.builtins.bytes;

import certik.congzhang.tool.codeql.solidity.builtins.uint.uint;

import java.math.BigInteger;

public class bytes{n} implements Ibytes {{
    private static final int SIZE = {n};
    private byte[] bytes = new byte[SIZE];

    public bytes{n}() {{

    }}

    public bytes{n}(Object o) {{

    }}

    @Override
    public int length() {{
        return SIZE;
    }}

    @Override
    public byte get(int index) {{
        return bytes[index];
    }}
    
    public byte get(uint o) {{
        return bytes[o.value().intValue()];
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
    with open(os.path.join('./', f'bytes{i}.java'), 'w') as f:
        f.write(template.format(n=i))
