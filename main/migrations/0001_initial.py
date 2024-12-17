# Generated by Django 5.1.4 on 2024-12-17 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('age', models.IntegerField()),
                ('avatar', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=20000)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint_about_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=10000)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints_about_this_post', to='main.post')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint_about_posts', to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint_about_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=10000)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints_about_this_comment', to='main.post')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint_about_comments', to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=10000)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.post')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Voting_variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='main.user')),
                ('variant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='main.voting_variant')),
            ],
        ),
    ]
