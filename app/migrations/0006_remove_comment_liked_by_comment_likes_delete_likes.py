# Generated by Django 4.0.5 on 2022-07-06 18:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_likes_by_comment_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
