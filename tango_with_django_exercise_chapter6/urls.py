"""tango_with_django_project_2539644 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# project's urls.py 的作用是分段处理URL 
    # 例如在http://www.abc.com/rango/index
    # 主机地址、域名是http://www.abc.com/
    # project's urls.py中处理rango/
    # rango app's urls.py中处理index

from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # MAPPING TO THE APP (rango.urls.py)
    # http://127.0.0.1:8000


    # 把空字符串Mapping到index视图: 
    # 当用户访问了http://www.abc.com/rango，即用户URL匹配了'/rango'模式时, 
    # Django就先使用project's urls处理URL(即/rango), 处理时去掉/rango部分，然后得到null, 再把null传给app's urls
    # 传递给app's urls后，# 传递给app's urls后，app's urls寻找自身匹配null的path(), 即path('',...,...)
    # 匹配到后，调用index() view, 这指明了需要处理的入站请求函数
    path('', views.index, name='index'), 

    # 把about字符串Mapping到about视图
    # 当用户访问了http://www.abc.com/rango/about，即用户URL匹配了'/rango/about'模式时, 
    # Django就先使用project's urls处理URL(即/rango/about), 处理时去掉/rango部分，然后得到/about, 
    # 把/about传给app's urls
    # 传递给app's urls后，app's urls寻找自身匹配/about的path(), 即path('/about',...,...)
    # 匹配到后，调用about() view, 指明需要处理的入站请求函数
    # path('about/', views.about, name='about'),

    # 把所有'rango/'开头的URL交给app rango去处理
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

