from django.urls import path
from . import views

'''类视图方式'''
urlpatterns = [
    path('list/', views.BlogListView.as_view(), name='list'),
    path('detail/<int:blog_id>/', views.BlogDetailView.as_view(), name='detail'),
]

'''函数视图方式'''
# urlpatterns = [
#     path('list/', views.blog_list,name='list'),
#     path('detail/<int:blog_id>/', views.blog_detail,name='detail'),
# ]
