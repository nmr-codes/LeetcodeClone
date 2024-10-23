from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('auth/login/')
        else:
            login(request, user)
            return redirect('/')
    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        last_name = request.POST.get('last_name', '')  # 'last_name' dan qiymat olish

        if password != confirm_password:
            messages.error(request, "Parollar bir xil emas!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu foydalanuvchi nomi band.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email manzili band.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password, last_name=last_name)  # last_name ni qo'shish
        user.save()
        messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
        return redirect('login_page')

    return render(request, 'auth/register.html')

def logout_view(request):
    logout(request)
    return redirect('/') 