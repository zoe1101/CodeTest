# coding:utf-8
from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):  #创建数据模型
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()

# 请求体
@app.post("/items/")
async def create_item(item: Item): #声明请求体参数
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# 请求体 + 路径参数
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# 请求体 + 路径参数 + 查询参数
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):  #FastAPI 会把 q 当作可选参数
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

if __name__ == '__main__':
    uvicorn.run(app='api请求:app', host="127.0.0.1", port=8000, reload=True)