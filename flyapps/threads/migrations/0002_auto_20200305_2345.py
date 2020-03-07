# Generated by Django 3.0.3 on 2020-03-05 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('threads', '0001_initial'),
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='threadview',
            name='viewed_by',
            field=models.ManyToManyField(related_name='thread_views', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='threadparticipant',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='threads.Thread'),
        ),
        migrations.AddField(
            model_name='threadparticipant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='threadedit',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_edits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='threadedit',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_edits', to='threads.Thread'),
        ),
        migrations.AddField(
            model_name='thread',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='categories.Category'),
        ),
        migrations.AddField(
            model_name='thread',
            name='starter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='thread',
            name='viewer',
            field=models.ManyToManyField(related_name='_thread_viewer_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='threads.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='threads.Thread'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(fields=['id', 'slug'], name='threads_thr_id_1505ab_idx'),
        ),
    ]
