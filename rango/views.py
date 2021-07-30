
# 从 django.http 模块中导入 HttpResponse对象
<<<<<<< HEAD
from django.http import HttpResponse

from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

=======
<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
=======
from django.http import HttpResponse
from django.shortcuts import render
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143

# 在view.py中，一个函数就是一个视图，这里编写名叫index的视图；
# 每个视图函数至少包含一个参数，也就是一个HttpResponse对象，也就是说视图函数必须返回一个HttpResponse对象
# HttpResponse对象的参数是一个字符串，所以在此index视图函数中，参数是字符串"Rango says hey there partner!!!"
# 参数名叫request
def index(request):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    context_dict['extra'] = 'From the model solution on GitHub'
<<<<<<< HEAD
=======
=======
    # Construct a dictionary tp pass to the template engine as tis context
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupacake!"}

    # Return a rendered response to send to the client
    # para: request对象、模板、context字典
    # 工作原理：render()函数把cotext字典中的数据代入模板，然后生成完整的html页面，作为HttpResponse对象返回，分发给Web浏览器
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
    return render(request, 'rango/index.html', context=context_dict)

# about视图函数 or about view method，参数名request 
def about(request):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
    # context_dict = {'boldmessage': "This tutorial has been put together by Chongjin ZHANG"}
    return render(request, 'rango/about.html')
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")


# show_category视图函数 or show_category view method，para: request 
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
<<<<<<< HEAD
        
=======
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    
    return render(request, 'rango/category.html', context=context_dict)
<<<<<<< HEAD

def add_category(request):
    form = CategoryForm()
    # is that HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # is form data valid?
        if form.is_valid():
            # save the new inputted category to the database
            form.save(commit=True)
            # redirect users go to the INDEX VIEW!
            return redirect('/rango/')
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None
    
    # Category does not exist (YES) create a new page for that
    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)  # This could be better done; for the purposes of TwD, this is fine. DM.
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)
=======
=======
    context_dict = {'boldmessage': "This tutorial has been put together by Chongjin ZHANG"}
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
