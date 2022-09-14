# 向管理页面中加入投票应用
# 只需要再做一件事：我们得告诉管理，问题 ​Question ​对象需要一个后台接口。

from django.contrib import admin

from .models import Question

admin.site.register(Question)