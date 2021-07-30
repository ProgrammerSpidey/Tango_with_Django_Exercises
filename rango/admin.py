from django.contrib import admin

<<<<<<< HEAD
from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)
=======
# Register your models here.
>>>>>>> add260af5eb7ac4706136378fe8eb6f3c6029adb
