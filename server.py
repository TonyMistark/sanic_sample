import time
from sanic import Sanic
from sanic.response import json

app = Sanic("My app")

@app.route("/hello")
async def test(request):
    print("enter test")
    time.sleep(1)
    print("end")
    return json({"hello": "hello"})

@app.route("/world")
async def test(request):
    print("enter test")
    time.sleep(1)
    print("end")
    return json({"world": "world"})

if __name__ == "__main__":
    app.run()
