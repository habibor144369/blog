from django.shortcuts import render
from .models import Post, IP
from django.views.generic import ListView, DetailView
from django .db.models import Q

# Create your views here.

class StudentList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'obj'
    

class ArticalsDetailsView(DetailView):
    model = Post
    template_name = 'articals_details.html'
    context_object_name = 'object'
    


def Hello(request):
    user = IP.objects.all()
 
    def Get_IP(request):
        address = request.META.get('HTTP_X_FORWORDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()

        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip=Get_IP(request)
    u=IP(user=ip)
    print(ip)

    result = IP.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exist")

    elif len(result)>1:
        print("user exist more.....")

    else:
        u.save()
        print("user is unique")

    count = IP.objects.all().count()
    print("total use is count")

    return render(request, 'views.html', {"user":user, "count":count})