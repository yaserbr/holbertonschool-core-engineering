#!/usr/bin/env python3
"""Web socket programming"""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    try:
        connected_clients.add(websocket)
        async for item in websocket:
            for client in connected_clients:
                await client.send(f"B:{item}")
    finally:
        connected_clients.remove(websocket)


async def main():
    print("leststing on port 8765")

    async with serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
