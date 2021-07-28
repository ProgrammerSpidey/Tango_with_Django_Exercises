
# 从 django.http 模块中导入 HttpResponse对象
from django.http import HttpResponse
from django.shortcuts import render

# 在view.py中，一个函数就是一个视图，这里编写名叫index的视图；
# 每个视图函数至少包含一个参数，也就是一个HttpResponse对象，也就是说视图函数必须返回一个HttpResponse对象
# HttpResponse对象的参数是一个字符串，所以在此index视图函数中，参数是字符串"Rango says hey there partner!!!"
# 参数名叫request
def index(request):
    return HttpResponse("Rango says hey there partner!!! <a href='/rango/about/'>About</a>")


# about视图函数 or about view method，参数名request 
def about(request):
    return HttpResponse("Rango says here is the about page!!! <a href ='/rango/'>Index</a>")