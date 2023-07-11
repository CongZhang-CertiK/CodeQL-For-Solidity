import os

# Java代码模板
template = """
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class uint{0} implements uint {{
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow({0}).subtract(BigInteger.ONE);

    public uint{0}(BigInteger value) {{
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {{
            throw new IllegalArgumentException("Value is out of range for uint{0}");
        }}
        this.value = value;
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

    @Override
    public uint add(uint other) {{
        return new uint{0}(this.value().add(other.value()));
    }}

    @Override
    public uint subtract(uint other) {{
        return new uint{0}(this.value().subtract(other.value()));
    }}

    @Override
    public uint multiply(uint other) {{
        return new uint{0}(this.value().multiply(other.value()));
    }}

    @Override
    public uint divide(uint other) {{
        return new uint{0}(this.value().divide(other.value()));
    }}

    @Override
    public uint mod(uint other) {{
        return new uint{0}(this.value().mod(other.value()));
    }}

    @Override
    public uint pow(uint exponent) {{
        return new uint{0}(this.value().pow(exponent.value().intValue()));
    }}

    @Override
    public uint and(uint other) {{
        return new uint{0}(this.value().and(other.value()));
    }}

    @Override
    public uint or(uint other) {{
        return new uint{0}(this.value().or(other.value()));
    }}

    @Override
    public uint xor(uint other) {{
        return new uint{0}(this.value().xor(other.value()));
    }}

    @Override
    public uint not() {{
        return new uint{0}(this.value().not());
    }}

    @Override
    public uint shiftLeft(int n) {{
        return new uint{0}(this.value().shiftLeft(n));
    }}

    @Override
    public uint shiftRight(int n) {{
        return new uint{0}(this.value().shiftRight(n));
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
