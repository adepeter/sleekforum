# Generated by Django 3.1.3 on 2020-11-27 16:07

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import sleekapps.threads.modelurls.post
import sleekapps.threads.modelurls.thread


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Post content')),
                ('is_hidden', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='likes')),
                ('dislikes', models.PositiveIntegerField(default=0, verbose_name='dislikes')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['created'],
                'get_latest_by': 'created',
            },
            bases=(models.Model, sleekapps.threads.modelurls.post.PostModelURL),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='title')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, help_text='Thread tags separated by comma', null=True, size=8)),
                ('pin', models.IntegerField(choices=[(0, 'Do not pin thread'), (1, 'Pin thread within category'), (2, 'Pin thread globally')], default=0, verbose_name='pin thread')),
                ('prefix', models.IntegerField(choices=[(0, 'Default'), (1, 'Help'), (2, 'Discussion'), (3, 'Info')], default=0, verbose_name='prefix')),
                ('slug', models.SlugField(blank=True, editable=False, verbose_name='slug')),
                ('content', models.TextField(unique_for_date='created', verbose_name='content')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_locked', models.BooleanField(default=False, verbose_name='lock thread')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='hide thread')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('sads', models.PositiveIntegerField(default=0)),
                ('happies', models.PositiveIntegerField(default=0)),
                ('wows', models.PositiveIntegerField(default=0)),
                ('angries', models.PositiveIntegerField(default=0)),
                ('funnies', models.PositiveIntegerField(default=0)),
                ('loves', models.PositiveIntegerField(default=0)),
                ('shares', models.PositiveIntegerField(default=0)),
                ('views', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(limit_choices_to=models.Q(is_lock=False), on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='categories.category', verbose_name='category')),
            ],
            options={
                'ordering': ['-modified'],
            },
            bases=(models.Model, sleekapps.threads.modelurls.thread.ThreadModelURL),
        ),
    ]
