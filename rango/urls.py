
# Handle the remaining URL string 
# and map the empty string to the index view

# 导入Django处理URL映射的函数
from django.urls import path

# 导入Rango应用的views模块
from rango import views

app_name = 'rango'

# 在urlspatterns列表中调用url函数映射index视图
<<<<<<< HEAD

=======
urlpatterns = [
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD

    # http://127.0.0.1:8000/rango
    path('', views.index, name='index'),

=======
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
>>>>>>> 5a1af3180eaac20e2f0dd7e254270ecd07a3db7d
    # 1st para: String to match, Empty String, 
    #   Django only find a match if there is nothing after http://127.0.0.1:8000/
    # 2nd para: Tells Django what view should to call when the pattern '' is matched
    # 3rd para: optiona, it is name, we can reference the URL mapping by name rather than URL itself
<<<<<<< HEAD
    # http://127.0.0.1:8000/rango/
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
=======
<<<<<<< HEAD
    # http://127.0.0.1:8000/rango/
=======
    # http://127.0.0.1:8000/rango
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
    path('', views.index, name='index'),


    # 1st para: String to match, 'about/' String, 
    #   Django only find a match if there is '/about' after http://127.0.0.1:8000/
    # 2nd para: Tells Django what view should to call when the pattern 'about/' is matched
<<<<<<< HEAD
    # http://127.0.0.1:8000/rango/about/
    path('about/', views.about, name='about'),

    # http://127.0.0.1:8000/category/computers/
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),

    # http://127.0.0.1:8000/add_category
    path('add_category/', views.add_category, name='add_category'),

    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
=======
<<<<<<< HEAD
    # http://127.0.0.1:8000/rango/about
    path('about/', views.about, name='about'),

    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
=======
>>>>>>> add260af5eb7ac4706136378fe8eb6f3c6029adb
    # http://127.0.0.1:8000/rango/about
    path('about/', views.about, name='about'),
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
>>>>>>> 5a1af3180eaac20e2f0dd7e254270ecd07a3db7d
]


