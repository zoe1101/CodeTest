import uvicorn
from fastapi import FastAPI,Path
from pydantic import BaseModel, EmailStr

app=FastAPI()
@app.get('/')
async def home():
    return {"message": "Hello World"}

'''
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


# uvicorn 是一个 ASGI 服务器。默认端口为 8000 ，默认 host 为 localhost。http://127.0.0.1:8000。打开 127.0.0.1:8000/docs 即可测试。使用 docs 的测试结果
uvicorn.run(app=app)
# uvicorn.run(app, host="127.0.0.1", port=8000)