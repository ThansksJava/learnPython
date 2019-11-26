import asyncio


async def hello():
    print("Hello World")
    r = await asyncio.sleep(1)
    print("Hello Again")

loop = asyncio.get_event_loop()
task = [hello(),hello()]
loop.run_until_complete(asyncio.wait(task))
loop.close()
