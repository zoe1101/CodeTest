from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['author']

    # list_dispaly用于设置列表页面要显示的不同字段
    list_display = ['title', 'author']

    # 添加搜索功能
    search_fields = ['title', 'content', 'author__username', 'author_first_name', 'author__lastname']

    def save_model(self, request, obj, form, change):
        if not change:  # 如果不是修改，也就是“新建”的时候
            obj.author = request.user
        super(BlogAdmin, self).save_model(request, obj, form, change)
