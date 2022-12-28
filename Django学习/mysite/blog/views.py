from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.core.paginator import Paginator # 引入分页组件
from .models import Blog

from django.views import generic

'''
基于类的视图实现方式
'''
class BlogListView(generic.ListView):
    model=Blog
    paginate_by = 20 #每页条数

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size') or self.paginate_by

    def render_to_response(self, context, **response_kwargs):
        paginator = context['paginator']
        current_page = context['page_obj']
        blogs=current_page.object_list

        data = {
            'blog_list': [
                {
                    'id': blog.id,
                    'title': blog.title,
                } for blog in blogs
            ],
            'paginator':{
                'total_count':paginator.count,
                'num_pages':paginator.num_pages,
                'page_size':paginator.per_page,
                'page_number':current_page.number,
            }
        }
        return JsonResponse(data)

class BlogDetailView(generic.DetailView):
    model = Blog

    def render_to_response(self, context, **response_kwargs):
        blog = context['object']

        data = {
            'blog': {
                'id': blog.id,
                'title': blog.title,
                'content': blog.content,
                'author': {
                    'id': blog.author.id,
                    'username': blog.author.username,
                }
            }
        }
        return JsonResponse(data)





'''
基于函数的视图实现方式
'''
# def blog_list(request):
#     page = request.GET.get('page',1) #第几页，默认第一页
#     page_size=request.GET.get('page_size',20)  #默认每页20条
#     blog_qs = Blog.objects.all()
#     paginator=Paginator(blog_qs,page_size)
#     current_page=paginator.get_page(page)
#
#     blogs=current_page.object_list
#
#     context = {
#         'blog_list': [
#             {
#                 'id': blog.id,
#                 'title': blog.title,
#             } for blog in blogs
#         ],
#         'paginator':{
#             'total_count':paginator.count,
#             'num_pages':paginator.num_pages,
#             'page_size':paginator.per_page,
#             'page_number':current_page.number,
#         }
#     }
#
#     return JsonResponse(context)
#
#
# def blog_detail(request, blog_id):
#     blog = Blog.objects.get(id=blog_id)
#     context = {
#         'blog': {
#             'id': blog.id,
#             'title': blog.title,
#             'content': blog.content,
#             'author': {
#                 'id': blog.author.id,
#                 'username': blog.author.username,
#             }
#         }
#     }
#     return JsonResponse(context)
