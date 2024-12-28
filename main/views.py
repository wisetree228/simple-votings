from django.shortcuts import render, redirect
from main.forms import SignInForm

# Create your views here.
def test_view(request):
    form = SignInForm()
    context={}
    context['form'] = form
    return render(request=request, template_name='login.html', context=context)