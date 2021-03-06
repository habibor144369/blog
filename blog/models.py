from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=150) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    key = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    
    def __str__(self):
        return self.title + ' author - ' + str(self.author) 


    def save(self, *args, **kwargs):
        self.slug = slugify([str(self.title), self.author, str(self.date), str(self.key)])
        super(Post, self).save(*args, **kwargs)



class IP(models.Model):
    user = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)

    def __str__(self):
        return self.user

    
class Information(models.Model):
    name = models.CharField(max_length=50)
    name2 = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    profation = models.CharField(max_length=150)
    age = models.IntegerField()
    phone = models.IntegerField()
    country = models.CharField(max_length=50)
    distric = models.CharField(max_length=50)
    gila = models.CharField(max_length=50)
    thana = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    relegion = models.CharField(max_length=30)
  
    
    def __str__(self):
        return self.name



        