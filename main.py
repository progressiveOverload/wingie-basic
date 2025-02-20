from typing import Union, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None



items = {}  # Store items in memory (replace with a database in a real application)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id in items:
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    global items
    if item_id in items:
        items[item_id] = item
        return items[item_id]
    else:
        return {"error": "Item not found"}


@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    global items
    items[item_id] = item
    return items[item_id]


@app.get("/items/", response_model=List[Item])
def read_all_items(skip: int = 0, limit: int = 10):
    item_list = list(items.values())
    return item_list[skip : skip + limit]