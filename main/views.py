from django.shortcuts import render, redirect
from main.forms import *
from hashlib import sha256
from main.models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages
from json import dumps

# Create your views here.
def login(request):
    """
    Представление для страницы авторизации. Форма принимает email и пароль,
    в случае неправильного ввода пароля или email показывает пользователю соответствующее представление об ошибке.
    После успешной авторизации перенаправляет пользователя на страницу с лентой постов
    Args:
        request (HttpRequest): request
    Returns:
        HttpResponse
    """
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
    """
    Представление для страницы регистрации. Форма принимает имя, фамилию, юзернейм, email и пароль,
    если аккаунт с данным юзернеймом/почтой уже существует, выдаёт пользователю соответствующее сообщение об ошибке.
    После успешной регистрации производит автоматическую авторизацию в только что созданный аккаунт
    и перенаправляет пользователя на страницу с лентой постов.
    Args:
        request (HttpRequest): request
    Returns:
        HttpResponse
    """
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
    """
    Представление выхода. После выхода перенаправляет на начальную страницу с
    выбором регистрации или входа (index)
    Args:
        request (HttpRequest): request
    Returns:
        HttpResponseRedirect
    """
    if not(request.user.is_authenticated):
        return redirect('index')
    logout(request)
    return redirect('index')

def index(request):
    """
    Начальная страница, предоставляет выбор между регистрацией и авторизацией
    Args:
        request (HttpRequest): request
    Returns:
        HttpResponse
    """
    if request.user.is_authenticated:
        return redirect(main_posts)
    return render(request, 'index.html', context={})


def main_posts(request):
    """
    Страница отображения ленты постов
    Args:
        request (HttpRequest): request
    Returns:
        HttpResponse
    """
    if not(request.user.is_authenticated):
        return redirect(index)

    context = {}
    posts_from_db = Post.objects.all()
    posts = []
    for post_db in posts_from_db:
        variants=[]
        vars_db = post_db.variants.all()
        for var in vars_db:
            variants.append(
                {
                    'text':var.text,
                    'id':var.id,
                }
            )
        post = {
            'author':post_db.author.username,
            'text':post_db.text,
            'variants':variants,
            'created_at':post_db.created_at,
        }
        posts.append(post)
    context['posts'] = posts
    #print(dumps(posts, indent=4, ensure_ascii=False))



    return render(request, 'posts.html', context=context)


def create_post(request):
    """
    Страница создания поста (голосования)
    Args:
        request (HttpRequest): request
    Returns:
        HttpResponse
    """
    if not(request.user.is_authenticated):
        return redirect(index)
    if request.method == 'POST':
        title = request.POST.get('title')
        options = request.POST.getlist('options[]')

        if len(options) < 2:
            messages.error(request, 'Минимум 2 варианта голосования!')
        else:
            voting = {
                    'title': title,
                    'options': options,
            }
            auth = User.objects.get(username=request.user.username)
            post = Post(author = auth, text = voting['title'])
            post.save()
            for var in voting['options']:
                opt = VotingVariant(text=var, post = post)
                opt.save()

    return render(request, 'create.html', context={})