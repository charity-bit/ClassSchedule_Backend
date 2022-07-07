# Generated by Django 4.0.5 on 2022-07-05 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_session_no_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_comments', to='app.session'),
        ),
    ]