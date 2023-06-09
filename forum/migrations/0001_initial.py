# Generated by Django 4.2.2 on 2023-06-15 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, default='-', help_text='<small class="text-muted">автор поста</small><hr><br>', max_length=200, null=True, verbose_name='Автор')),
                ('title', models.CharField(blank=True, default='-', help_text='<small class="text-muted"></small><hr><br>', max_length=200, null=True, unique=True, verbose_name='Заголовок поста')),
                ('text', models.TextField(blank=True, default='-', help_text='<small class="text-muted"></small><hr><br>', null=True, unique=True, verbose_name='Описание поста')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, help_text='<small class="text-muted">время создания поста</small><hr><br>', verbose_name='Дата и время создания')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ('-datetime', 'title'),
            },
        ),
    ]
