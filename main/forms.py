from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)

class SignInForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)