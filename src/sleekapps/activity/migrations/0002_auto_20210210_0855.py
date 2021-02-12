# Generated by Django 3.1.6 on 2021-02-10 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_reactions', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddConstraint(
            model_name='reaction',
            constraint=models.UniqueConstraint(fields=('user', 'reaction', 'content_type', 'object_id'), name='unique_user_activity'),
        ),
    ]