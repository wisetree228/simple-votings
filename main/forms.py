from django import forms


class RegisterForm(forms.Form):
    """
    Представление для страницы регистрации. Форма принимает email, пароль, username,
    name, surname.
    После успешной регистрации перенаправляет пользователя на страницу с лентой постов.
    Args:
        forms.Form
    Returns:
        HttpResponse
    """

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-group",
        'placeholder': 'input name'
    }),
        label='Name', max_length=255)
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-group",
        'placeholder': 'input surname'
    }),
        label='Surname', max_length=255)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-group",
        'placeholder': 'input username'
    }),
        label='Username', max_length=255)
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-group",
        'placeholder': 'input email'
    }),
        label='Email', max_length=255)
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-group",
        'placeholder': 'input password'
    }),
        label='Password', max_length=255)


class SignInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': "form-group",
            'placeholder': 'input email'
        }),
        label='Email', max_length=255
    )
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-group",
        'placeholder': 'input password'
    }),
        label='Password', max_length=255
    )
