# coding:utf-8
from typing import List, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 使用路径操作装饰器的参数 response_model 定义响应模型，可以过滤数据，特别适合用来保护隐私数据。
# 只返回显式设置过的值时，可以使用 response_model_exclude_unset 参数。
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.post("/items/", response_model=Item)  #response_model参数定义响应
async def create_item(item: Item):
    return item


if __name__ == '__main__':
    uvicorn.run(app='api响应:app', host="127.0.0.1", port=8000, reload=True)