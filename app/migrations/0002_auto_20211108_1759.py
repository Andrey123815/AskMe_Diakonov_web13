# Generated by Django 3.2.9 on 2021-11-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='rating',
        ),
        migrations.AddField(
            model_name='question',
            name='dislikes_count',
            field=models.IntegerField(default=0, verbose_name='Дизлайки'),
        ),
        migrations.AddField(
            model_name='question',
            name='likes_count',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='likequestion',
            name='is_like',
            field=models.BooleanField(default=True, verbose_name='Лайк'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='img/no_avatar.jpeg', upload_to='static/avatar/%y/%m/%d', verbose_name='Аватар'),
        ),
    ]
