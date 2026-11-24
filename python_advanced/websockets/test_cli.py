#!/usr/bin/env python3

import asyncio
from websockets.asyncio.client import connect


async def receive_messages(ws):
    async for message in ws:
        print(f"\nReceived: {message}")


async def main():
    async with connect("ws://localhost:8000/ws") as ws:
        asyncio.create_task(receive_messages(ws))

        while True:
            message = await asyncio.to_thread(input, "> ")

            if message == "exit":
                break

            await ws.send(message)


if __name__ == "__main__":
    asyncio.run(main())
