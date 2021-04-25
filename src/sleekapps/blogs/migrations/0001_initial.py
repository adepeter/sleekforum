# Generated by Django 3.1.6 on 2021-04-25 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, editable=False, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_locked', models.BooleanField(default=True, help_text='If locked, users cannot see add post or         make alteration to articles/posts in this category totally', verbose_name='Lock')),
                ('is_hidden', models.BooleanField(default=False, help_text='If hidden, users cannot see article in this category totally', verbose_name='Hide')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, editable=False, verbose_name='Slug')),
                ('content', models.TextField(blank=True, help_text='If content is not entered, its marked as draft', null=True, verbose_name='article body')),
                ('completion_status', models.IntegerField(choices=[(0, 'draft'), (1, 'completed')], default=0, editable=False, help_text='Choose status of blog default is DRAFT', verbose_name='completion Status')),
                ('is_locked', models.BooleanField(default=True, verbose_name='Lock')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='Hide')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogs', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blogs.category', verbose_name='category')),
            ],
        ),
    ]
