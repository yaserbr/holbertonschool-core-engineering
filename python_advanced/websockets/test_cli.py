#!/usr/bin/env python3

import asyncio
from websockets.asyncio.client import connect


async def main():
    async with connect("ws://127.0.0.1:8765") as websocket:
        while True:
            message = await asyncio.to_thread(input, "> ")

            if message == "exit":
                break

            await websocket.send(message)
            response = await websocket.recv()
            print(f"< {response}")


if __name__ == "__main__":
    asyncio.run(main())
