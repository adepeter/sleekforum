# Generated by Django 3.1.6 on 2021-02-25 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('is_read', models.BooleanField(default=False, verbose_name='is read')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='date sent')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='chats.privatemessage', verbose_name='parent message')),
            ],
            options={
                'ordering': ['id'],
                'get_latest_by': 'date_sent',
            },
        ),
    ]
