#!/usr/bin/env python3
import struct
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
#后面的参数个数要和处理指令一致
print(struct.pack('>I',10240099))
#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))
#https://docs.python.org/3/library/struct.html#format-characters



