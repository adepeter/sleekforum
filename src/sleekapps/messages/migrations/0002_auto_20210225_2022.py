# Generated by Django 3.1.6 on 2021-02-25 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='privatemessage',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages_received', to=settings.AUTH_USER_MODEL, verbose_name='recipient'),
        ),
        migrations.AddField(
            model_name='privatemessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages_sent', to=settings.AUTH_USER_MODEL, verbose_name='sender'),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('chats.privatemessage',),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('chats.privatemessage',),
        ),
        migrations.CreateModel(
            name='PrivateChat',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('chats.privatemessage',),
        ),
    ]
