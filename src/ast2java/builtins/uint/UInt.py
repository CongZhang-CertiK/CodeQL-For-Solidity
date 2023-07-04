import os

# Java代码模板
template = """
package certik.congzhang.tool.codeql.solidity.builtins.uint;

import java.math.BigInteger;

public class UInt{0} implements UInt {{
    private BigInteger value;

    private static final BigInteger MAX_VALUE = BigInteger.valueOf(2).pow({0}).subtract(BigInteger.ONE);

    public UInt{0}(BigInteger value) {{
        if (value.signum() < 0 || value.compareTo(MAX_VALUE) > 0) {{
            throw new IllegalArgumentException("Value is out of range for UInt{0}");
        }}
        this.value = value;
    }}

    @Override
    public BigInteger value() {{
        return value;
    }}

    @Override
    public UInt add(UInt other) {{
        return new UInt{0}(this.value().add(other.value()));
    }}

    @Override
    public UInt subtract(UInt other) {{
        return new UInt{0}(this.value().subtract(other.value()));
    }}

    @Override
    public UInt multiply(UInt other) {{
        return new UInt{0}(this.value().multiply(other.value()));
    }}

    @Override
    public UInt divide(UInt other) {{
        return new UInt{0}(this.value().divide(other.value()));
    }}

    @Override
    public UInt mod(UInt other) {{
        return new UInt{0}(this.value().mod(other.value()));
    }}

    @Override
    public UInt pow(UInt exponent) {{
        return new UInt{0}(this.value().pow(exponent.value().intValue()));
    }}

    @Override
    public UInt and(UInt other) {{
        return new UInt{0}(this.value().and(other.value()));
    }}

    @Override
    public UInt or(UInt other) {{
        return new UInt{0}(this.value().or(other.value()));
    }}

    @Override
    public UInt xor(UInt other) {{
        return new UInt{0}(this.value().xor(other.value()));
    }}

    @Override
    public UInt not() {{
        return new UInt{0}(this.value().not());
    }}

    @Override
    public UInt shiftLeft(int n) {{
        return new UInt{0}(this.value().shiftLeft(n));
    }}

    @Override
    public UInt shiftRight(int n) {{
        return new UInt{0}(this.value().shiftRight(n));
    }}
}}
"""

# 创建目录路径
path = './'
os.makedirs(path, exist_ok=True)

# 生成并写入文件
for i in range(8, 256+1, 8):
    file_name = f"UInt{i}.java"
    with open(os.path.join(path, file_name), 'w') as f:
        f.write(template.format(i))
