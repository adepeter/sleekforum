# Generated by Django 3.1.6 on 2021-02-12 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('is_read', models.BooleanField(default=False, verbose_name='is read')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='date sent')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='chats.privatemessage', verbose_name='parent message')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages_received', to=settings.AUTH_USER_MODEL, verbose_name='recipient')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages_sent', to=settings.AUTH_USER_MODEL, verbose_name='sender')),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
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
    ]
