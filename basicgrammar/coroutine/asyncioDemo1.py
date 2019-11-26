import asyncio
import threading


@asyncio.coroutine
def hello():
    print("Hello World(%s)" % threading.currentThread().name)
    r = yield from asyncio.sleep(1)
    print("Hello Again(%s)" % threading.currentThread().name)


loop = asyncio.get_event_loop()
task = [hello(), hello()]
loop.run_until_complete(asyncio.wait(task))
loop.close()
