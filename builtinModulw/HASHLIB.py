#!/usr/bin/env python3
import hashlib

#md5 128 bits,通常用32字节的十六进制字符串表示
md5=hashlib.md5()
#如果数据很长,多次挑勇update(),最后计算结果和一次调用也是相同的
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())

#sha1 160 bits ,通常用40字节的十六进制字符串表示

sha1=hashlib.sha1()
sha1.update("how to use sha1 in python hashlib".encode('utf-8'))
print(sha1.hexdigest())

