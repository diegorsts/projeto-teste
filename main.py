from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste": "deu certo"}