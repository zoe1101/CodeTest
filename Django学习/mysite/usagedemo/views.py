from django.http import HttpResponse


# 1.创建视图
# 2.将视图路由添加到全局路由中

def index(request): #定义一个叫做index的视图函数
    """
    request:是HttpResponse对象，前端的请求信息会全部传递给这个参数request
    return:必须返回一个HttpResponse对象或者子对象
    """
    return HttpResponse("<h1>Hello Wold！</h1>")

