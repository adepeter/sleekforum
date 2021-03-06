# Generated by Django 3.1.6 on 2021-04-25 12:07

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_auto_20210425_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, help_text='Thread tags separated by comma', null=True, size=8),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='comment body')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='hide')),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blogs.article', verbose_name='article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_comments', to=settings.AUTH_USER_MODEL, verbose_name='poster')),
            ],
        ),
    ]
