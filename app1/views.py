from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ServiceRequestForm 

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Пароли не совпадают')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Логин уже занят')
            return redirect('signup')
            
        phone = request.POST['phone']
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.save()
        profile = Employee.objects.create(user=user, phone=phone)
        profile.save()
        return redirect('/login')
    return render(request, 'signup.html')

def login_auth(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Неправильный логин или пароль')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_auth(request):
    logout(request)
    return redirect('/')

def index(request):
    return render(request, 'index.html')

@login_required
def service(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user if request.user.is_authenticated else None
            service_request.save()
            return redirect('/')
        else:
            return render(request, 'service.html', {'form': form})
    else:
        form = ServiceRequestForm()
    return render(request, 'service.html', {'form': form})

@login_required
def service_list(request):
    user_req = ServiceRequest.objects.filter(user=request.user).order_by('id')
    return render(request, 'service_list.html', {'user_req': user_req})