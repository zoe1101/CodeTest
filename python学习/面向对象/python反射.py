class TestObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test(self):
        print("ִ��test����")


def a():
    print("����ⲿ����")


if __name__ == '__main__':
    """1.getattr ��ȡ�������ԡ����󷽷�"""
    xiaoyu = TestObject("С��", 20)
    # ��ȡ���������
    print(getattr(xiaoyu, "name"))
    # ��ȡ����ķ���
    result = getattr(xiaoyu, "test")
    print(type(result))
    result()
    """2.hasattr �ж϶����Ƿ��ж�Ӧ�����ԡ�����"""
    if hasattr(xiaoyu, "address"):
        print(getattr(xiaoyu, "address"))
    if hasattr(xiaoyu, "name"):
        print(getattr(xiaoyu, "name"))
    """3.delattr ɾ������"""
    # delattr(xiaoyu,"name")
    """4.setattr Ϊ������������"""
    # �޸����Ե�ֵ
    setattr(xiaoyu, "name", "liuwei")
    print(getattr(xiaoyu, "name"))
    # �޸ķ���
    setattr(xiaoyu, "test11", a)
    getattr(xiaoyu, "test11")()
    # �൱��������test11����
    xiaoyu.test11()
"""
ȥʵ��ĳ��ҵ�񣬶����࣬�������װ�˺ܶ෽�����ṩһ��ͳһ������ܹ����ø��ַ���
ҵ�񣺵�¼   �˳�  ע��  ע��
"""


class Test:
    func_list = ["login", "loginOut", "register", "delete"]

    def login(self):
        print("���ǵ�¼")

    def loginOut(self):
        print("�����˳�")

    def register(self):
        print("����ע��")

    def delete(self):
        print("����ע��")

    # 1.login    2.loginOut  3.register  4.delete
    def run(self, num):
        getattr(self, self.func_list[num - 1])()


num = int(input("��������Ĳ���(1.login    2.loginOut  3.register  4.delete):"))
Test().run(num)