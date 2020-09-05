# Generated by Django 3.1 on 2020-09-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='website title', max_length=20, verbose_name='site title')),
                ('email', models.EmailField(default='noreply@localhost', max_length=254, verbose_name='e-mail')),
                ('welcome_mail', models.TextField(blank=True, help_text='message after successful registration', verbose_name='welcome message')),
                ('allow_registration', models.BooleanField(default=True)),
                ('captcha', models.BooleanField(default=False, help_text='Turn on/off captcha on pages')),
                ('threads_per_page', models.PositiveSmallIntegerField(default=10)),
                ('posts_per_thread', models.PositiveSmallIntegerField(default=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
