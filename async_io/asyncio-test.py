#!/usr/bin/env python3
#asyncio 是Python3.4版本引入的标准库,直接内置对异步io的支持
#asyncio 的变成模型是一个消息循环,
import asyncio
@asyncio.coroutine
def hello():
	print("hello,world")
	r=yield from asyncio.sleep(1)
	print('hello,again')
loop=asyncio.get_event_loop()
loop.run_until_complete(hello())
print('main')
loop.close()


