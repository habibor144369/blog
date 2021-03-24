from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=600) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    key = models.CharField(max_length=600, unique=True)
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
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    profation = models.CharField(max_length=150)
    age = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

        