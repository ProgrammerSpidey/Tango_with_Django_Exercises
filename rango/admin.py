<<<<<<< HEAD


# Register your models here.

from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
=======
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
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
