# Generated by Django 3.2.5 on 2021-07-23 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0005_auto_20210425_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='action_by',
            field=models.ForeignKey(default=None, help_text='User who triggered the notifications action', on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='users.user', verbose_name='Action performed by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='alert',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
