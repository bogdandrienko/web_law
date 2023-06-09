# Generated by Django 4.2.2 on 2023-06-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('is_success', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Запрос к юристам',
                'verbose_name_plural': 'Запросы к юристам',
                'ordering': ('is_success', '-datetime', 'title'),
            },
        ),
    ]
