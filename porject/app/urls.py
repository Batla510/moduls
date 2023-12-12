from django.urls import path
from .views import index,login,register,data,posts

urlpatterns = [
    path('',index,name='home'),
    path('login',login,name='Login'),
    path('register',register,name='Register'),
    path('data',data,name="data"),
    path('post',posts,name='posts')
]