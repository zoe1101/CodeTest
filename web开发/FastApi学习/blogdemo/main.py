import os
from pathlib import Path

import pandas as pd
import uvicorn
from fastapi import FastAPI

# 导入Request上下文对象，用来在前后台之间传递参数
from starlette.requests import Request

# 导入jinja2模板引擎对象，用于后续使用
from starlette.templating import Jinja2Templates

app = FastAPI()

# 实例化一个模板引擎对象，指定模板所在路径
templates = Jinja2Templates(directory="templates")
data_path = os.path.abspath(Path("data"))
# 获取文件路径
file_path = os.path.join(data_path, "learning.xlsx")


# 在视图函数中传入request对象，用于在模板对象中传递上下文（同时接收路径参数info，将其传递到上下文中）
@app.get("/", summary="这是一个模板渲染示例")
async def index(request: Request):
    # 加载excel数据
    result = pd.read_excel(file_path)
    # 将excel数据转化为JSON对象
    info = result.to_dict("records")
    # 返回一个模板对象，同时使用上下文中的数据对模板进行渲染
    return templates.TemplateResponse(
        name="index.html", context={"request": request, "info": info}
    )


@app.get("/index/async", summary="这是一个异步接口")
def index_async():
    return {"key": "这是一个异步接口返回的数据"}


@app.get("/index", summary="这是一个同步接口")
def index():
    return {"key": "这是一个同步接口返回的数据"}


if __name__ == "__main__":
    # 启动程序
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)

'''

http://localhost:8000/
# 文档地址：
http://localhost:8000/docs
http://localhost:8000/redoc

'''
