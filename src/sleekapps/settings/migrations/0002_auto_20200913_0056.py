# Generated by Django 3.1 on 2020-09-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='description',
            field=models.TextField(blank=True, verbose_name='site description'),
        ),
        migrations.AddField(
            model_name='setting',
            name='send_welcome_mail',
            field=models.BooleanField(default=False, help_text='Send welcome mail to new users', verbose_name='send welcome email'),
        ),
        migrations.AddField(
            model_name='setting',
            name='under_maintenance',
            field=models.BooleanField(default=False, help_text='Determine if site is under maintenance', verbose_name='maintenance status'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='captcha',
            field=models.BooleanField(default=False, help_text='Turn on/off captcha on pages', verbose_name='captcha verification'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='posts_per_thread',
            field=models.PositiveSmallIntegerField(default=10, help_text='Number of posts to display per thread', verbose_name='posts per thread'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='threads_per_page',
            field=models.PositiveSmallIntegerField(default=10, help_text='Number of threads to show on a page', verbose_name='threads on a page'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(default='sleekforum', help_text='website title', max_length=20, verbose_name='site title'),
        ),
    ]
