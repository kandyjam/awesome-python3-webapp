from aiohttp import web

from www.coroweb import get


@get('/index')
def handler_url_index():
    print("index page")
    return '<h1>Awesome python web 程序</h1>'
