from aiohttp import web
import json

from foo import storage


async def index(request):
    bars = await storage.get_some_bar()
    bars = {
        "id": bars[0],
        "name": bars[1],
        "created_at": bars[2].isoformat(),
    }
    return web.Response(body=json.dumps(bars).encode())
