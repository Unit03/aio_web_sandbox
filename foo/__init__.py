from aiohttp import web

from foo import settings
from foo import views


app = web.Application(debug=settings.DEBUG)
app.router.add_route("GET", "/", views.index)


def main():
    web.run_app(app, port=settings.LISTEN_PORT)
