from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    """
    Модель пользователя, наследуется от AbstractUser. Поля можно и не обьяснять, и так понятно что для чего
    """
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255) # если что тут будет храниться хэш, а не сам пароль
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    avatar = models.ImageField(null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    """
    Модель поста. Имеет сам текст поста (вопрос голосования) и автора
    """
    text = models.TextField(max_length=20000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VotingVariant(models.Model):
    """
    Модель варианта голосования, привязан к посту. Имеет текст и пост в котором находится
    """
    text = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='variants')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Vote(models.Model):
    """
    Модель голоса, связывает вариант голосования и пользователя который за него проголосовал
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    variant = models.ForeignKey(VotingVariant, on_delete=models.CASCADE, related_name='votes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    """
    Модель комментария под постом, имеет поля поста под которым оставлен, текст и автора
    """
    text = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ComplaintAboutPost(models.Model):
    """
    Модель жалобы на пост, данный функционал на данный момент не реализован и нигде не используется
    """
    text = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaint_about_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='complaints_about_this_post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ComplaintAboutComment(models.Model):
    """
    Модель жалобы на комментарий, данный функционал на данный момент не реализован и нигде не используется
    """
    text = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaint_about_comments')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='complaints_about_this_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    """
    Модель лайка, связывает пост и пользователя который его лайкнул
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')

