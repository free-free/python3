#!/usr/bin/env python3
#asyncio实现TCP,UDP,SSL等协议,aiohttp则是基于asyncio实现的HTTP框架
#使用aiohttp需要先安装


#用aiohttp编写一个http服务器

import asyncio
from aiohttp import web
async def index(request):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>Index</h1>')

async def yes(request):
	await asyncio.sleep(0.5)
	text='<h1>yes,%s!</h1>'%request.match_info['name']
	return web.Response(body=text.encode('utf-8'))

async def init(loop):
	app=web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	app.router.add_route('GET','/yes/{name}',yes)
	srv=await loop.create_server(app.make_handler(),'121.42.169.254',8000)
	print('Server started at http://121.42.169.254:80...')
	return srv
if __name__=='__main__':
	loop=asyncio.get_event_loop()
	loop.run_until_complete(init(loop))
	loop.run_forever()

	
