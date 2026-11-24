#!/usr/bin/env python3
"""Web socket programming"""

import uvicorn
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def web_socketConnection(socket):
    await socket.accept()
    async for item in socket.iter_text():
        print(item)
        await socket.send_text(item)


app = Starlette(
    routes=[Route("/", homepage), WebSocketRoute("/ws", web_socketConnection)]
)
if __name__ == "__main__":
    uvicorn.run("asgi_server:app", host="0.0.0.0", port=8000, reload=True)
