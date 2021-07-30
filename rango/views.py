
# 从 django.http 模块中导入 HttpResponse对象
from django.http import HttpResponse
from django.shortcuts import render

# 在view.py中，一个函数就是一个视图，这里编写名叫index的视图；
# 每个视图函数至少包含一个参数，也就是一个HttpResponse对象，也就是说视图函数必须返回一个HttpResponse对象
# HttpResponse对象的参数是一个字符串，所以在此index视图函数中，参数是字符串"Rango says hey there partner!!!"
# 参数名叫request
def index(request):
    # Construct a dictionary tp pass to the template engine as tis context
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupacake!"}

    # Return a rendered response to send to the client
    # para: request对象、模板、context字典
    # 工作原理：render()函数把cotext字典中的数据代入模板，然后生成完整的html页面，作为HttpResponse对象返回，分发给Web浏览器
    return render(request, 'rango/index.html', context=context_dict)

# about视图函数 or about view method，参数名request 
def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Chongjin ZHANG"}
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")