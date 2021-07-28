
# Handle the remaining URL string 
# and map the empty string to the index view

# 导入Django处理URL映射的函数
from django.urls import path

# 导入Rango应用的views模块
from rango import views

app_name = 'rango'

# 在urlspatterns列表中调用url函数映射index视图
urlpatterns = [
    # 1st para: String to match, Empty String, 
    #   Django only find a match if there is nothing after http://127.0.0.1:8000/
    # 2nd para: Tells Django what view should to call when the pattern '' is matched
    # 3rd para: optiona, it is name, we can reference the URL mapping by name rather than URL itself
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
]


