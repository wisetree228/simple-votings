from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)

class SignInForm(forms.Form):
    email = forms.EmailField(
    widget=forms.TextInput(attrs = {
        'class': "form-group",
        'placeholder': 'input email'
    }),
    label='Email', max_length=255
    )
    password = forms.CharField(    widget=forms.TextInput(attrs = {
        'class': "form-group",
        'placeholder': 'input password'
    }),
    label='Password', max_length=255
    )