import time
import asyncio
import requests

async def req():
    print("enter req")
    await requests.get("http://127.0.0.1:8000/")
    print("finish request--->")

if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [req() for i in range(1000)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(f"cost seconds: {time.time() - start}")
