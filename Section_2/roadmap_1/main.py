import fastapi
import uvicorn

print("Hello fastapi")
api = fastapi.FastAPI()


@api.get('/api/endpoint')
def endpoint():
    return {"msg": "Hello api/endpoint"}


@api.get("/")
def index():
    return{"msg": "hello world ",
           "another msg": ["hello", "world"]}


@api.get("/api/pass_data2/{x}")
def pass_data2(x):
    print(x, type(x))
    return {"x": x}


@api.get("/api/pass_data1")
def pass_data1(x: int, y):
        print(x, y)
        print(type(x), type(y))
        return {"x": x, "y": y, "x+y": int(x)+int(y)}


@api.get("/html")
def index():
    body = '''
    <html>
    <body>Body</body>
    </html>
    '''
    return fastapi.responses.HTMLResponse(content=body)


if __name__ == "__main__":
    uvicorn.run("main:api", port=9000, host='127.0.0.1', reload=True)
