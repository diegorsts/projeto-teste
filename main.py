from fastapi import FastAPI
import random

app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# 127.0.0.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    return{"teste": True, "num_aleatorio": random.randint(0, 20000)}