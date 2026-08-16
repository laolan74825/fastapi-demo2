from typing import Annotated, List

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/")
async def get_items(q: Annotated[List[str], Query(deprecated=True)]):
    return {"items": [q[0], q[1], q[2]]}
