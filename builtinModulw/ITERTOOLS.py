#!/usr/bin/env python3
import itertools
#count 会创建一个无限的迭代器
natuals=itertools.count(1)
for n in natuals:
	print(n)
	if n>10:
		break

#cycle 会把传入的一个序列无限循环下去
cs=itertools.cycle('ABC')
for c in cs:
	print(c)
	if c =='C':
		break
#repeat 负责把一个元素无限重复下去
ns=itertools.repeat('X',2)
for n in ns:
	print(n)

#无限序列只有在for迭代时才会无限的迭代下去,通过takeWhile()截取一个有限序列
natuals=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))

#chain()可以把一组迭代对象串联起来,形成一个更大的迭代器
for c in itertools.chain('ABV','ZYD'):
	print(c)

#groupby() 把迭代器中相邻的重复的元素挑出来放在一起
for key,group in itertools.groupby('AAANNNDSSD'):
	print(key,list(group))


