<<<<<<< HEAD
from typing import Tuple
from django.db import models

# Create your models here.
'''
A class = A model
Each class inherits father class, django.db.models.Model
'''

class Category(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=128, unique=True)
    # Exercise
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)


class Page(models.Model):

    def __str__(self):
        return self.title

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    
=======
from django.db import models

# Create your models here.
>>>>>>> add260af5eb7ac4706136378fe8eb6f3c6029adb
