# Generated by Django 3.0.3 on 2020-03-05 22:45

from django.db import migrations, models
import flyapps.users.managers.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('username', models.CharField(max_length=25, unique=True, verbose_name='username')),
                ('username_slug', models.SlugField(blank=True, verbose_name='username slug')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('sex', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('dob', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=75)),
                ('signature', models.TextField(blank=True)),
                ('threads', models.PositiveIntegerField(default=0)),
                ('comments', models.PositiveIntegerField(default=0)),
                ('is_hide_presence', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('phone_number', models.PositiveIntegerField(default=0)),
                ('website', models.URLField(blank=True, default='https://')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['email'],
            },
            managers=[
                ('objects', flyapps.users.managers.user.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('email', 'username_slug'), name='unique_user'),
        ),
    ]
