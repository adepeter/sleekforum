# Generated by Django 3.1.6 on 2021-04-24 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20210424_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='threadview',
            options={'verbose_name': 'Viewer', 'verbose_name_plural': 'Viewers'},
        ),
    ]