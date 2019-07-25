import logging;

logging.basicConfig(level=logging.INFO)

import asyncio

from aiohttp import web


def index(request):
    print("index page")
    return web.Response(text='<h1>Awesome</h1>', content_type='text/html')


async def init(event_loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    runner = web.AppRunner(app)
    await runner.setup()
    srv = web.TCPSite(runner, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000 ...')
    await srv.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
