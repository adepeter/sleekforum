# Generated by Django 3.1.6 on 2021-02-26 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='friendrequest',
            index=models.Index(fields=['id'], name='friends_fri_id_f18b60_idx'),
        ),
        migrations.AddConstraint(
            model_name='friendrequest',
            constraint=models.UniqueConstraint(fields=('request_from', 'request_to'), name='unique_friend_request'),
        ),
    ]
