#!/usr/bin/env python3
"""Web socket programming"""

import asyncio
from websockets.asyncio.server import serve


async def connection_handler(websocket):

    async for item in websocket:
        print("User says : " + item)
        await websocket.send(item)


async def main():
    print("leststing on port 8765")

    async with serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
