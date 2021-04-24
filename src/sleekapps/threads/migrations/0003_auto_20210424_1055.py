# Generated by Django 3.1.6 on 2021-04-24 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0002_auto_20210225_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_views', to='threads.thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_views', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='threadview',
            constraint=models.UniqueConstraint(fields=('thread', 'user'), name='unique_thread_user_on_thread_view'),
        ),
    ]
