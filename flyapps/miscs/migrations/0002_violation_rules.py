# Generated by Django 3.0.5 on 2020-05-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rules', '0001_initial'),
        ('miscs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='violation',
            name='rules',
            field=models.ManyToManyField(related_name='violations', related_query_name='violations', to='rules.Rule', verbose_name='rules violated'),
        ),
    ]
