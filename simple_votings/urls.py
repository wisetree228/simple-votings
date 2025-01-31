"""
URL configuration for simple_votings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('posts/', main_posts, name='posts'),
    path('create/', create_post, name='create'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comments/<int:post_id>', comments, name='comments'),
    path('profile/', profile_view, name='profile'),
    path('whovoted/<int:id>', option_voters, name='whovoted'),
    path('liked/', liked, name='liked'),
    path('my_votings/', my_posts, name='my_votings')
]
