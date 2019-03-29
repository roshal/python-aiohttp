import aiohttp

async def handle(request):
	name = request.match_info.get('name', 'Anonymous')
	return aiohttp.web.Response(**{
		text: ''.join(('hello', name)),
	})

app = aiohttp.web.Application()
app.add_routes([
	aiohttp.web.get('/', handle),
	aiohttp.web.get('/{name}', handle),
])
aiohttp.web.run_app(app)
