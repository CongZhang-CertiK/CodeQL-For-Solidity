import os

# 定义Java文件的模板
java_template = """package certik.congzhang.tool.codeql.solidity.builtins.bytes;

public class Bytes{0} implements IBytes {{
    private int n = {0};
    private byte[] bytes = new byte[{0}];

    public Bytes{0}() {{

    }}

    @Override
    public int length() {{
        return n;
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
        if (n != this.n) {{
            throw new IllegalArgumentException("Cannot convert to a different bytesN type");
        }}
        return bytes.clone();
    }}

    @Override
    public void fromBytesN(byte[] bytesN) {{
        if (bytesN.length != n) {{
            throw new IllegalArgumentException("Size of bytesN does not match N");
        }}
        System.arraycopy(bytesN, 0, bytes, 0, n);
    }}
}}
"""

# 要生成文件的目录
directory = './'  # 请替换为你的目录路径

# 生成从1到32的BytesN.java文件
for i in range(1, 33):
    java_file_content = java_template.format(i)
    with open(os.path.join(directory, f'Bytes{i}.java'), 'w') as f:
        f.write(java_file_content)
