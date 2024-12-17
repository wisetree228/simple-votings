from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255) # если что тут будет храниться хэш, а не сам пароль
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    avatar = models.BinaryField()

class Post(models.Model):
    text = models.TextField(max_length=20000)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

class Voting_variant(models.Model):
    text = models.CharField(max_length=300)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='variants')

class Vote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    variant_id = models.ForeignKey(Voting_variant, on_delete=models.CASCADE, related_name='votes')

class Comment(models.Model):
    text = models.TextField(max_length=10000)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

class Complaint_about_post(models.Model):
    text = models.TextField(max_length=10000)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaint_about_posts')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='complaints_about_this_post')

class Complaint_about_comment(models.Model):
    text = models.TextField(max_length=10000)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaint_about_comments')
    comment_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='complaints_about_this_comment')