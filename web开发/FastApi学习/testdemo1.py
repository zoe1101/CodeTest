from pydantic import BaseModel
from datetime import date


# 把变量声明为字符串
# 在函数内部获得编辑器支持
def main(user_id: str):
    return user_id


class User(BaseModel):
    id: int
    name: str
    joined: date


my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

