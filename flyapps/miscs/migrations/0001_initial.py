# Generated by Django 3.0.7 on 2020-06-09 14:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('action_value', models.CharField(choices=[('FAV', 'Favorite'), ('LIK', 'Like'), ('DSL', 'Dislike'), ('UVT', 'Up Vote'), ('DVT', 'Down Vote')], max_length=3, verbose_name='Action')),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('is_violated', models.IntegerField(choices=[(0, 'Awaiting actions'), (1, 'Accepted violation'), (2, 'Rejected violation')], default=0, verbose_name='accept violation')),
                ('reported_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='reported on')),
                ('penalty', models.IntegerField(choices=[(0, 'No action'), (1, 'Hide object'), (2, 'Ban user'), (3, 'Delete object and Ban User')], default=0, help_text='Proper measure to be taken against violation', verbose_name='penalty')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
