# Generated by Django 3.1.6 on 2021-04-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20210425_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, upload_to='blogs/covers', verbose_name='cover image'),
        ),
    ]