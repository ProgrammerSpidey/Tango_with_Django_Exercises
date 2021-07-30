
# Handle the remaining URL string 
# and map the empty string to the index view

<<<<<<< HEAD
from django.urls import path

=======
# 导入Django处理URL映射的函数
from django.urls import path

# 导入Rango应用的views模块
>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066
from rango import views

app_name = 'rango'

<<<<<<< HEAD
    # 1st para: String to match, Empty String, 
    #   Django only find a match if there is nothing after http://127.0.0.1:8000/
    # 2nd para: Tells Django what view should to call when the pattern '' is matched
    # 3rd para: optiona, it is name, we can reference the URL mapping by name rather than URL itself
=======
>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
]


