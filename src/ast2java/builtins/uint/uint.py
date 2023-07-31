import os

# Java代码模板
template = """
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint{0} implements uint {{
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow({0}).subtract(BigInteger.ONE);

    public uint{0}(Object o) {{
        this.value = new BigInteger(String.valueOf(o));
    }}
    
    public uint{0}(int value) {{
        this(BigInteger.valueOf(value));
    }}

    public uint{0}(long value) {{
        this(BigInteger.valueOf(value));
    }}

    @Override
    public BigInteger value() {{
        return value;
    }}
}}
"""

# 创建目录路径
path = './'
os.makedirs(path, exist_ok=True)

# 生成并写入文件
for i in range(8, 256+1, 8):
    file_name = f"uint{i}.java"
    with open(os.path.join(path, file_name), 'w') as f:
        f.write(template.format(i))
