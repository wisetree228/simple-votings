from django.shortcuts import render, redirect
from main.forms import *
from hashlib import sha256
from main.models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.
def login(request):
    form = SignInForm()
    context={}
    context['form'] = form
    if request.method=='POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if User.objects.filter(email=email).exists():
                username = User.objects.get(email=email).username
                user = authenticate(request, username=username, password=password)
                if user:
                    auth_login(request, user)
                    return redirect(main_posts)
                else:
                    messages.error(request,
                                   'Неверный пароль!')
            messages.error(request, 'Аккаунта с таким email не существует! Проверьте корректность или зарегистрируйтесь')
    return render(request=request, template_name='login.html', context=context)

def register(request):
    form = RegisterForm()
    context={}
    context['form'] = form
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if not(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                user = User(username = username, name = name, surname = surname, email = email)
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                if user:
                    auth_login(request, user)
                    return redirect(main_posts)
            else:
                messages.error(request, 'Ошибка регистрации, пользователь с такой почтой и/или юзернеймом существует!')

    return render(request=request, template_name='register.html', context=context)



def logout_view(request):
    logout(request)
    return redirect(main_posts)

def index(request):
    if request.user.is_authenticated:
        return redirect(main_posts)
    return render(request, 'index.html', context={})


def main_posts(request):
    if not(request.user.is_authenticated):
        return redirect(index)
    return render(request, 'posts.html', context={})