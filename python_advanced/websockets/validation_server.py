#!/usr/bin/env python3
"""Web socket programming"""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):

    async for item in websocket:
        temp = item.strip()
        if len(temp) == 0:
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{item}")


async def main():
    print("leststing on port 8765")

    async with serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
