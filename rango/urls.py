
# Handle the remaining URL string 
# and map the empty string to the index view

# 导入Django处理URL映射的函数
from django.urls import path

# 导入Rango应用的views模块
from rango import views

app_name = 'rango'

# 在urlspatterns列表中调用url函数映射index视图
urlpatterns = [

    # http://127.0.0.1:8000/rango
    path('', views.index, name='index'),

    # http://127.0.0.1:8000/rango/about
    path('about/', views.about, name='about'),
]


