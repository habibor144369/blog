from django.contrib import admin
from.models import Post, IP, Information

# Register your models here.



class PersonAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date', 'slug', 'key']
    list_per_page = 15
    search_fields = ['title']
    list_filter = ['title', 'date', 'key']

class Details(admin.ModelAdmin):
    list_display = ['name', 'name2', 'email', 'profation', 'country', 'relegion']
    search_fields = ['name', 'email']
    list_filter = ['name', 'email', 'address', 'phone']

admin.site.register(Post, PersonAdmin)
admin.site.register(IP)
admin.site.register(Information, Details)

