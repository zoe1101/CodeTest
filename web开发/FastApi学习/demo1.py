from typing import Optional

import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

app = FastAPI()  # 创建一个 FastAPI「实例」


@app.get('/')  # 定义一个路径操作装饰器
async def home():  # 也可以将其定义为常规函数而不使用 async def
    return {"message": "Hello World"}


# 可以使用与 Python 格式化字符串相同的语法来声明路径"参数"或"变量",路径参数 item_id 的值将作为参数 item_id 传递给你的函数
@app.get("/items/{item_id}")
async def read_item(item_id: int):  # 可以使用标准的 Python 类型标注为函数中的路径参数声明类型。
    return {"item_id": item_id}


'''
在这个例子中，有3个查询参数：
needy，一个必需的 str 类型参数。
skip，一个默认值为 0 的 int 类型参数。
limit，一个可选的 int 类型参数。
'''


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):  # 查询参数 传参
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


'''
请求体，使用 Pydantic 模型来声明请求体
在函数中，定义参数为 user: UserIn 表明需要输入的数据符合 UserIn 模型。配置 response_model 为 UserOut ，表明输出数据符合 UserOut 模型。FastApi 会自动进行过滤
'''


class UserIn(BaseModel):
    username: str
    password: str
    age: int
    full_name: str = None


class UserOut(BaseModel):
    username: str
    age: int
    full_name: str = None


@app.post("/user/", response_model=UserOut)
async def create_user(*, user: UserIn):
    return user


'''
请求体 + 路径参数 + 查询参数
'''


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# uvicorn 是一个 ASGI 服务器。默认端口为 8000 ，默认 host 为 localhost。http://127.0.0.1:8000。打开 127.0.0.1:8000/docs 即可测试。使用 docs 的测试结果
uvicorn.run(app=app)
# uvicorn.run(app, host="127.0.0.1", port=8000)
