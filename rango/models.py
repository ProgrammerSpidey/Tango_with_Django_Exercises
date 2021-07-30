<<<<<<< HEAD
from typing import Tuple
from django.db import models
from django.template.defaultfilters import slugify
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
from typing import Tuple
from django.db import models
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143

# Create your models here.
'''
A class = A model
Each class inherits father class, django.db.models.Model
'''

class Category(models.Model):
<<<<<<< HEAD
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
=======
<<<<<<< HEAD
=======
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704

    name = models.CharField(max_length=128, unique=True)
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
    # Exercise
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
    slug = models.SlugField(unique=True)
   # slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
<<<<<<< HEAD
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
=======
=======

class Page(models.Model):

    def __str__(self):
        return self.title
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

<<<<<<< HEAD
    def __str__(self):
        return self.title
=======
    
=======
from django.db import models

# Create your models here.
>>>>>>> add260af5eb7ac4706136378fe8eb6f3c6029adb
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
>>>>>>> d5ce4d19dbaca42306851f15ac469f0ce0346143
