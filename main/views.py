from django.shortcuts import render, redirect
from main.forms import *
from main.models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from main.log import logger
# Create your views here.
def login(request):
    """
    Представление для страницы авторизации. Форма принимает email и пароль,
    в случае неправильного ввода пароля или email показывает пользователю соответствующее представление об ошибке.
    После успешной авторизации перенаправляет пользователя на страницу с лентой постов
    Args:
        request: HttpRequest
    Returns:
        HttpResponse
    """
    logger.info("запущена программа логина")
    form = SignInForm()
    context = {}
    context['form'] = form # форма авторизации подаётся через контекст
    if request.method == 'POST': # обработка отправки формы
        try:
            form = SignInForm(request.POST)
            logger.info("Форма сгенерирована в штатном режиме")
        except:
            logger.error('Ошибка в генерации формы')
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password') # получаем значения из формы
            if User.objects.filter(email=email).exists(): # проверка существования пользователя с таким email, если нет то соответствующее сообщение об ошибке
                username = User.objects.get(email=email).username # далее стандартная авторизация джанго, логгирование и переход на страницу с лентой постов
                user = authenticate(request, username=username, password=password)
                if user:
                    logger.info(f"Пользователь {username} вошёл в аккаунт")
                    auth_login(request, user)
                    return redirect(main_posts)
                else:
                    messages.error(request,
                                   'Неверный пароль!')
            messages.error(request,
                           'Аккаунта с таким email не существует! Проверьте корректность или зарегистрируйтесь')
    return render(request=request, template_name='login.html', context=context)


def register(request):
    """
    Представление для страницы регистрации. Форма принимает имя, фамилию, юзернейм, email и пароль,
    если аккаунт с данным юзернеймом/почтой уже существует, выдаёт пользователю соответствующее сообщение об ошибке.
    После успешной регистрации производит автоматическую авторизацию в только что созданный аккаунт
    и перенаправляет пользователя на страницу с лентой постов.
    Args:
        request: HttpRequest
    Returns:
        HttpResponse
    """
    form = RegisterForm()
    context = {}
    context['form'] = form # форма авторизации подаётся через контекст
    if request.method == 'POST': # обработка отправки формы
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()): # если email или username занят то выдаём сообщение об ошибке в else
                user = User(username=username, name=name, surname=surname, email=email) # создаём юзера в бд, автоматически производим авторизацию в созданный аккаунт и перенаправляем пользователя на ленту постов
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                if user:
                    logger.info(f"Пользователь {username} зарегистрировался")
                    auth_login(request, user)
                    return redirect(main_posts)
            else:
                messages.error(request, 'Ошибка регистрации, пользователь с такой почтой и/или юзернеймом существует!')

    return render(request=request, template_name='register.html', context=context)


def logout_view(request):
    """
    Представление выхода из аккаунта. После выхода перенаправляет на начальную страницу с
    выбором регистрации или входа (index)
    Args:
        request: HttpRequest
    Returns:
        HttpResponseRedirect
    """
    if not request.user.is_authenticated: # если пользователь и так не авторизован то просто перенаправляем его в индекс
        return redirect('index')
    logout(request) # иначе выход из аккаунта и редирект в индекс
    logger.info(f"пользователь {request.user.username} вышел из аккаунта")
    return redirect('index')


def index(request):
    """
    Начальная страница для неавторизованного пользователя, предоставляет выбор между регистрацией и авторизацией
    Args:
        request: HttpRequest
    Returns:
        HttpResponse
    """
    if request.user.is_authenticated: # если пользователь уже вошёл в аккаунт перенаправляем его на ленту постов
        return redirect(main_posts)
    return render(request, 'index.html', context={})


def main_posts(request):
    """
    Страница отображения ленты постов. Можно ставить лайки, голосовать в постах, переходить к
    просмотру поста (читать и писать комментарии и смотреть процентные результаты голосования). Если
    пользователь не авторизован, его перекидывает на начальную страницу (index). Имеет работающий на бэкенде поиск
    Args:
        request: HttpRequest
    Returns:
        HttpResponse
    """
    if not request.user.is_authenticated:
        return redirect(index)

    context = {}
    posts_from_db = Post.objects.all() # достаём все посты из бд чтобы составить контекст
    posts = []
    form = SearchForm() # обработка поиска
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']
            posts_from_db = posts_from_db.filter(text__icontains=query)
    for post_db in posts_from_db: # составляем контекст
        variants = []
        vars_db = post_db.variants.all()
        for var in vars_db: # для каждого поста список его вариантов голосования
            variants.append(
                {
                    'text': var.text,
                    'id': var.id,
                }
            )
        post = { # делаем пост в формате json со всеми нужными для рендера данными
            'id': post_db.id,
            'author': post_db.author.username,
            'text': post_db.text,
            'variants': variants,
            'created_at': post_db.created_at,
            'likes_count': Like.objects.filter(post=post_db).count(),
            'comments_count': Comment.objects.filter(post=post_db).count(),
        }
        posts.append(post)
    context['posts'] = posts
    context['form'] = form
    context['user_liked_posts'] = Like.objects.filter(
        user=User.objects.get(username=request.user.username)).values_list('post_id', flat=True) # посты на которых уже стоит лайк пользователя

    if request.method == 'POST': # обработка голосования в посте
        selected_vote = request.POST.get('vote')
        vote_list = selected_vote.split('!!!')
        variant = VotingVariant.objects.get(id=int(vote_list[0])) # получаем нужный пост и вариант голосования
        user = User.objects.get(username=request.user.username)
        post = Post.objects.get(id=int(vote_list[1]))
        if VotingVariant.objects.filter(post=post).exists(): # проверяем, голосовал ли пользователь в этом посте, если да то предыдущий голос удаляем
            for var in post.variants.all():
                if Vote.objects.filter(variant=var, user=user).exists():
                    vote = Vote.objects.get(variant=var, user=user)
                    vote.delete()
            vote = Vote(user=user, variant=variant)
            vote.save()
            logger.info(f"пользователь {request.user.username} проголосовал, id поста{post.id} id варианта {variant.id}")

    return render(request, 'posts.html', context=context)


def create_post(request):
    """
    Страница создания поста (голосования). Можно создать пост-голосование и добавить сколько угодно каких угодно вариантов ответа
    Args:
        request: HttpRequest
    Returns:
        HttpResponse
    """
    if not request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST': # обработка отправки формы
        title = request.POST.get('title')
        options = request.POST.getlist('options[]')

        if len(options) < 2 or ('' in options): # ограничение на количество вариантов голосования
            messages.error(request, 'Минимум 2 не пустых варианта голосования!')
        else:
            auth = User.objects.get(username=request.user.username)
            post = Post(author=auth, text=title) # создаём сам пост
            post.save()
            for var in options: # добавляем все варианты голосования для этого поста
                opt = VotingVariant(text=var, post=post)
                opt.save()
            logger.info(f"пользователь {request.user.username} создал голосование с id {post.id}")
            return redirect('posts')

    return render(request, 'create.html', context={})


@csrf_exempt
@require_POST
def like_post(request, post_id):
    """
    Функция с помощью которой можно поставить лайк под постом.
    Args:
        request: HttpRequest
        post_id (int): id поста на который ставится лайк
    Returns:
        HttpResponse
    """
    if not request.user.is_authenticated: # обработка ошибки если пользователь не авторизован
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated'}, status=403)

    post = Post.objects.get(id=post_id)
    like, created = Like.objects.get_or_create(user=User.objects.get(username=request.user.username), post=post)
    # узнаём стоит ли лайк на посте, если да удаляем иначе добавляем
    if not created:
        like.delete()
        return JsonResponse({'status': 'unliked', 'likes_count': Like.objects.filter(post=post).count()})
    else:
        return JsonResponse({'status': 'liked', 'likes_count': Like.objects.filter(post=post).count()})


def comments(request, post_id):
    """
    Страница просмотра поста, процентных результатов голосования, чтения и написания комментариев под постом
    Args:
        request: HttpRequest
        post_id (int): id поста который смотрим
    Returns:
        HttpResponse
    """
    if not request.user.is_authenticated:
        return redirect('index')
    if not (Post.objects.filter(id=post_id).exists()):
        return redirect('posts')
    post = Post.objects.get(id=post_id)
    context = {}
    context['user_liked_posts'] = Like.objects.filter(
        user=User.objects.get(username=request.user.username)).values_list('post_id', flat=True)
    res = []
    count_of_votes = 0
    vars = post.variants.all()
    # считаем сколько людей проголосовало за все варианты и считаем проценты
    for var in vars:
        count_of_votes += Vote.objects.filter(variant=var).count()
    if count_of_votes != 0:
        for var in vars:
            res.append({
                'text': var.text,
                'percent': round((Vote.objects.filter(variant=var).count() / count_of_votes) * 100),
                'id':var.id,
            })
    else: # если голосов нет то везде 0 процентов
        for var in vars:
            res.append({
                'text': var.text,
                'percent': 0,
                'id': var.id,
            })
    comms = [] # составляем список комментариев под постом
    for comment in post.comments.all():
        comms.append({
            'text': comment.text,
            'author': comment.author.username,
            'created_at': comment.created_at,
        })
    context['post_text'] = post.text
    context['results'] = res
    context['comments'] = comms
    context['author'] = post.author.username
    context['post_id'] = post_id
    context['likes_count'] = Like.objects.filter(post=post).count()
    if request.method == 'POST': # обработка написания комментария
        text = request.POST.get('text')
        comm = Comment(text=text, author=User.objects.get(username=request.user.username), post=post)
        comm.save()
        return redirect('comments', post_id=post_id)

    return render(request, 'comment.html', context=context)

def profile_view(request):
    """
    Страница просмотра своего профиля и смены любых своих данных
    Args:
        request: HttpRequest
    Returns:
        HttpResponse
    """
    if not request.user.is_authenticated:
        return redirect('index')
    context = {}
    data_db = User.objects.get(username=request.user.username)
    user = {
        'id':data_db.id,
        'username':data_db.username,
        'name':data_db.name,
        'surname':data_db.surname,
        'email':data_db.email,
        'registered_at':data_db.created_at,
        }
    context['user'] = user # подаём данные пользователя в контекст
    if request.method == 'POST': # обработка смены данных
        user = User.objects.get(username=request.user.username)
        user.username = request.POST.get('username')
        print(request.POST.get('username'))
        user.name = request.POST.get('firstName')
        user.surname = request.POST.get('lastName')
        user.email = request.POST.get('email')
        if request.POST.get('newPassword'): # меняем данные которые подал пользователь, если в форме был новый пароль то меняем пароль и заново проводим авторизацию
            user.set_password(request.POST.get('newPassword'))
        user.save()
        user = authenticate(request, username=request.user.username, password=request.POST.get('newPassword'))
        if user:
            auth_login(request, user)
            return redirect('profile')
    return render(request, 'profile.html', context=context)


def option_voters(request, id: int):
    """
    Страница просмотра списка человек, которые голосовали за определённый вариант в голосовании
    Args:
        request: HttpRequest
        id (int): id варианта голосования
    Returns:
        HttpResponse
    """
    if not request.user.is_authenticated:
        return redirect('index')
    var_db = VotingVariant.objects.get(id=id)
    post_id = var_db.post.id
    context = {}
    users = [] # составляем массив пользователей которые голосовали за этот вариант
    for vote in Vote.objects.filter(variant=var_db):
        user = {
            'username':vote.user.username,
            'name': vote.user.name,
            'surname': vote.user.surname,
        }
        users.append(user)
    context['post_id'] = post_id
    context['users'] = users
    context['variant_text'] = var_db.text
    return render(request, 'whovoted.html', context)

def liked(request):
    """
    Страница просмотра лайкнутых постов, работает также как основная лента постов но там отображаются только посты которые пользователь лайкнул
    Args:
        request: HttpRequest
    Returns:
        HttpResponse
    """
    posts_db = []
    context = {}
    posts = []
    user = User.objects.get(username=request.user.username)
    context['user_liked_posts'] = Like.objects.filter(
        user=User.objects.get(username=request.user.username)).values_list('post_id', flat=True)
    for like in user.reactions.all():
        posts_db.append(like.post)
    form = SearchForm() # обработка поиска
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']
            posts_from_db = posts_db.filter(text__icontains=query)
    context['form'] = form
    for post_db in posts_db: # всё как на основной ленте, составляем словарь постов, но только лайкнутых
        variants = []
        vars_db = post_db.variants.all()
        for var in vars_db:
            variants.append(
                {
                    'text': var.text,
                    'id': var.id,
                }
            )
        post = {
            'id': post_db.id,
            'author': post_db.author.username,
            'text': post_db.text,
            'variants': variants,
            'created_at': post_db.created_at,
            'likes_count': Like.objects.filter(post=post_db).count(),
            'comments_count': Comment.objects.filter(post=post_db).count(),
        }
        posts.append(post)
    context['posts'] = posts
    if request.method == 'POST': # тут всё как на основной ленте
        selected_vote = request.POST.get('vote')
        vote_list = selected_vote.split('!!!')
        variant = VotingVariant.objects.get(id=int(vote_list[0]))
        user = User.objects.get(username=request.user.username)
        post = Post.objects.get(id=int(vote_list[1]))
        if VotingVariant.objects.filter(post=post).exists():
            # проверяем, голосовал ли пользователь в этом посте, если да то предыдущий голос удаляем
            for var in post.variants.all():
                if Vote.objects.filter(variant=var, user=user).exists():
                    vote = Vote.objects.get(variant=var, user=user)
                    vote.delete()
            vote = Vote(user=user, variant=variant)
            vote.save()
            logger.info(f"пользователь {request.user.username} проголосовал, id поста{post.id} id варианта {variant.id}")

    return render(request, 'liked.html', context)


def my_posts(request):
    """
    Страница просмотра своих постов, работает также как основная лента постов но там отображаются только посты которые пользователь создал сам
    Args:
        request: HttpRequest
    Returns:
        HttpResponse
    """
    posts_db = []
    context = {}
    posts = []
    user = User.objects.get(username=request.user.username)
    context['user_liked_posts'] = Like.objects.filter(
        user=User.objects.get(username=request.user.username)).values_list('post_id', flat=True)
    form = SearchForm() # обработка поиска
    user_posts = user.posts.all()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']
            user_posts = user_posts.filter(text__icontains=query)
    context['form'] = form
    for post_db in user_posts: # всё как на основной ленте, только собственные посты пользователя
        variants = []
        vars_db = post_db.variants.all()
        for var in vars_db:
            variants.append(
                {
                    'text': var.text,
                    'id': var.id,
                }
            )
        post = {
            'id': post_db.id,
            'author': post_db.author.username,
            'text': post_db.text,
            'variants': variants,
            'created_at': post_db.created_at,
            'likes_count': Like.objects.filter(post=post_db).count(),
            'comments_count': Comment.objects.filter(post=post_db).count(),
        }
        posts.append(post)
    context['posts'] = posts
    if request.method == 'POST':
        selected_vote = request.POST.get('vote')
        vote_list = selected_vote.split('!!!')
        variant = VotingVariant.objects.get(id=int(vote_list[0]))
        user = User.objects.get(username=request.user.username)
        post = Post.objects.get(id=int(vote_list[1]))
        if VotingVariant.objects.filter(post=post).exists():
            # проверяем, голосовал ли пользователь в этом посте, если да то предыдущий голос удаляем
            for var in post.variants.all():
                if Vote.objects.filter(variant=var, user=user).exists():
                    vote = Vote.objects.get(variant=var, user=user)
                    vote.delete()
            vote = Vote(user=user, variant=variant)
            vote.save()
            logger.info(f"пользователь {request.user.username} проголосовал, id поста{post.id} id варианта {variant.id}")

    return render(request, 'myvotings.html', context)
