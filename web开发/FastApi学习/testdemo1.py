from pydantic import BaseModel
from datetime import date


# �ѱ�������Ϊ�ַ���
# �ں����ڲ���ñ༭��֧��
def main(user_id: str):
    return user_id


class User(BaseModel):
    id: int
    name: str
    joined: date


my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

