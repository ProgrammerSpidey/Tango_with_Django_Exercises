
# 从 django.http 模块中导入 HttpResponse对象
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.shortcuts import render, redirect
from django.urls import reverse
<<<<<<< HEAD
from datetime import datetime

=======


# 在view.py中，一个函数就是一个视图，这里编写名叫index的视图；
# 每个视图函数至少包含一个参数，也就是一个HttpResponse对象，也就是说视图函数必须返回一个HttpResponse对象
# HttpResponse对象的参数是一个字符串，所以在此index视图函数中，参数是字符串"Rango says hey there partner!!!"
# 参数名叫request
>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    context_dict['extra'] = 'From the model solution on GitHub'
<<<<<<< HEAD
    
    visitor_cookie_handler(request)

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/about.html', context=context_dict)
=======
    return render(request, 'rango/index.html', context=context_dict)

# about视图函数 or about view method，参数名request 
def about(request):
    # context_dict = {'boldmessage': "This tutorial has been put together by Chongjin ZHANG"}
    return render(request, 'rango/about.html')
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    
    return render(request, 'rango/category.html', context=context_dict)
    
<<<<<<< HEAD
 
=======
# show_category视图函数 or show_category view method，para: request 
>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066
@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None
    
<<<<<<< HEAD

=======
>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066
    if category is None:
        return redirect(reverse('rango:index'))

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
<<<<<<< HEAD
            print(form.errors)
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)
    
=======
            print(form.errors) 
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)

@login_required
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
            print(form.errors) 
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)

>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066
def register(request):
    registered = False

    # Grab information from the raw form
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # If both froms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save from data
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # If not a HTTP POST
        # These from will be blank where ready for user imput
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', context={
        'user_form': user_form, 
        'profile_form': profile_form, 
        'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html')

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

@login_required
def user_logout(request):
    logout(request)
<<<<<<< HEAD
    return redirect(reverse('rango:index'))

# Appurtenance
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits
=======
    return redirect(reverse('rango:index'))
>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066
