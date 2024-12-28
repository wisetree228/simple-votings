from django.shortcuts import render, redirect
from main.forms import SignInForm

# Create your views here.
def login(request):
    form = SignInForm()
    context={}
    context['form'] = form
    return render(request=request, template_name='login.html', context=context)