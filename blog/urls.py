from django.urls import path
from .import views
from .views import StudentList, ArticalsDetailsView


urlpatterns = [
    # path('', views.StudentList.as_view(), name='home'),   // another methods 

    path('', StudentList.as_view(), name='home'),
    path('artical/<int:pk>/<slug:slug>/', ArticalsDetailsView.as_view(), name='artical'),
    path('hello/', views.Hello, name='hello'), 
]
