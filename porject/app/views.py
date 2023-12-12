from django.shortcuts import render, redirect
from .forms import UserForm,UserLogin,AddPost
from django.http import HttpResponse
from .models import Person,Posts

def posts(request):
    if request.method == 'POST':
        post = Posts.objects.all()
        return render(request, 'app/post.html',context={'posts':post})
    else:
        form = AddPost
        return render(request, 'app/post.html', context={'posts': post})
def data(request):
    tom = Person.obsects.get_or_create(name='Tom', age=14,date='2015-3-14 15:55:22',agree = True)
    # mike = Person(name='Mike', age=52,date='2012-03-14 16:66:22',agree = False)
    # mike.save()
    print(create)
    try:
        mike = Person(name='Mike', age=52, date='2012-03-14 16:66:22', agree=False)
         mike.delete()
    except:
        mike = Person(name='Mike', age=52,date='2012-03-14 16:66:22',agree = False)
        mike.save()
    data = Person.objects.filter(age__gt=20)
    return render(request,'app/data.html',context={'data':data})

def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            return HttpResponse(f'Name: {name},Age: {age},Email: {email}')
        else:
            return HttpResponse('Данные не валидны')
    else:
        form = UserForm
        return render(request,'app/index.html',context={'form': form})

def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            if email == 'User1@gmail.com' and password == "12345678":
                return HttpResponse('Поздравляю с успешным входом')
            else:
                return redirect('Register')
        else:
            return  HttpResponse('Фoрма инвалид')
    form = UserLogin
    return render(request,'app/login.html',context={'form':form})
def register(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            return HttpResponse(f'{name},поздравляю с регистрацией, \n указаные вами данные Name-{name},email-{email},password-{password}')
        else:
            return HttpResponse('Нельзя зарегаться')
    form = UserLogin
    return render(request,'app/reg.html',context={'form':form})
