# Generated by Django 3.0.4 on 2020-03-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20200307_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='is_editable',
            field=models.BooleanField(default=True, verbose_name='Allow edit'),
        ),
    ]