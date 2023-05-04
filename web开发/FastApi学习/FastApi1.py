# coding:utf-8
from typing import Union

import uvicorn
from fastapi import FastAPI  # 为 API 提供所有功能的 Python 类

app = FastAPI()  # FastAPI 的类实例


@app.get("/")
async def root():
    return {"message": "Hello World"}

# =========路径参数=============
@app.get("/items/{item_id}")  # http://127.0.0.1:8000/items/1
async def read_item(item_id: str):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":  #使用 ModelName.lenet.value 也能获取值 "lenet"
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# 路径转换器
@app.get("/files/{file_path:path}")  #参数名为 file_path，结尾部分的 :path 说明该参数应匹配路径
async def read_file(file_path: str):
    return {"file_path": file_path}


# =================查询参数====================
# 声明的参数不是路径参数时，路径操作函数会把该参数自动解释为查询参数。
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")  #例如：http://127.0.0.1:8000/items/?skip=0&limit=10 等同于  http://127.0.0.1:8000/items/
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):  #把默认值设为 None 即可声明可选的查询参数
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
# FastAPI 可以识别出 item_id 是路径参数，q 不是路径参数，而是查询参数。





if __name__ == '__main__':
    uvicorn.run(app='FastApi1:app', host="127.0.0.1", port=8000, reload=True)
    # 命令行执行：
    # uvicorn FastApi1:app  --reload    #--reload：代码更新后，重启服务器。仅在开发时使用
