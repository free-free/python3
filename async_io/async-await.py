#!/usr/bin/env python3
import asyncio
#python3.5中,将@asyncio.coroutine 用async代替
#yield from 用await 代替,试语法更加的简单
async def hello():
	print('hello')
	r=await asyncio.sleep(1)
	print('world')

if __name__=='__main__':
	loop=asyncio.get_event_loop()
	loop.run_until_complete(hello())
	loop.close()
