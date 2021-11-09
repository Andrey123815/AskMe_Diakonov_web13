# Generated by Django 3.2.9 on 2021-11-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_likequestion_is_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='likequestion',
            name='is_like',
            field=models.BooleanField(default=True, verbose_name='Лайк или дизлайк'),
        ),
    ]