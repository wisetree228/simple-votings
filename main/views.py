from django.shortcuts import render, redirect
from main.forms import *
from hashlib import sha256
from main.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    form = SignInForm()
    context={}
    context['form'] = form
    return render(request=request, template_name='login.html', context=context)

def register(request):
    form = RegisterForm()
    context={}
    context['form'] = form
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #form.save()
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
                    return redirect(testview)

    return render(request=request, template_name='register.html', context=context)

@login_required
def testview(request):
    if request.user.is_authenticated:
        context = {'username':request.user.username}
    else:
        context = {'username':'еруьу'}
    return render(request, 'testpage.html', context=context)