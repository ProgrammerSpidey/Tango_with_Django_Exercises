from typing import Tuple
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
'''
A class = A model
Each class inherits father class, django.db.models.Model
'''

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    # Exercise
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)
<<<<<<< HEAD
=======
   # slug = models.SlugField(blank=True)
>>>>>>> e6a63616fe330586b9b321bcde5d02de5a6e4066

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # links a user's profile to a user model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other informaiton (not compulsory)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username