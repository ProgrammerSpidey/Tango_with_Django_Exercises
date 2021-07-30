<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704
from typing import Tuple
from django.db import models

# Create your models here.
'''
A class = A model
Each class inherits father class, django.db.models.Model
'''

class Category(models.Model):
<<<<<<< HEAD
=======
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
>>>>>>> 2ae7d5a75d338512e46e2b14b596682f1f097704

    name = models.CharField(max_length=128, unique=True)
    # Exercise
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

<<<<<<< HEAD
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
