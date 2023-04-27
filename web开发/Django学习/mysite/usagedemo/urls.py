from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("index/", views.index)  # views.index是一个函数
    ]