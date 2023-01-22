from django.contrib.auth.models import User
from django.db import models

class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')



class Category(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)




class Image(models.Model):
    img = models.ImageField(upload_to='media/')


class Audio(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='audios/')



status = (
    ('simple', 'simple'),
    ('audio', 'audio'),
    ('new', 'new'),
)

class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=status)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ManyToManyField(Image, null=True, blank=True)
    language = models.CharField(max_length=200)
    audio = models.ManyToManyField(Audio, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(null=True, blank=True)
    page = models.IntegerField(null=True, blank=True)



class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
