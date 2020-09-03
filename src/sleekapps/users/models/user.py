import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.core.cache import cache
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ...cores.utils.choice import Choicify
from ...cores.validators import validate_image_filesize

from ..constants import user
from ..utils import ImageHandler
from ..managers.user import UserManager

avatar_handler = ImageHandler
choicify_sex = Choicify(user.GENDER_CHOICES)


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('e-mail'),
        unique=True
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=25,
        unique=True,
        db_index=True
    )
    avatar = models.ImageField(
        upload_to=avatar_handler.upload_to,
        blank=True,
        null=True,
        validators=[validate_image_filesize]
    )
    firstname = models.CharField(
        max_length=20,
        blank=True
    )
    middlename = models.CharField(
        max_length=20,
        blank=True
    )
    lastname = models.CharField(
        max_length=20,
        blank=True
    )
    sex = models.CharField(
        max_length=len(choicify_sex),
        choices=choicify_sex.get_choices,
        blank=True
    )
    dob = models.DateField(
        verbose_name=_('Date of Birth'),
        blank=True,
        null=True,
        help_text=_('Birth date in yyyy-mm-dd format')
    )
    about = models.TextField(
        verbose_name=_('About me'),
        max_length=500,
        blank=True,
        help_text=_('A description about you. Max: 500 chars')
    )
    hobbies = ArrayField(
        base_field=models.TextField(),
        verbose_name=_('Hobbies'),
        blank=True,
        null=True,
        help_text=_('Hobbies separated by comma')
    )
    phone_number = models.CharField(
        verbose_name=_('Phone number'),
        max_length=15,
        help_text=_('Phone number can start with + but no space'),
        blank=True
    )
    address = models.CharField(
        verbose_name=_('Address'),
        max_length=50,
        blank=True
    )
    state = models.CharField(
        verbose_name=_('State'),
        max_length=20,
        blank=True
    )
    country = models.CharField(
        max_length=20,
        blank=True
    )
    signature = models.TextField(
        blank=True,
        help_text=_('A short brief of you that will show in forum')
    )
    is_admin = models.BooleanField(
        verbose_name=_('Is admin'),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_('Is superuser'),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
    )
    date_created = models.DateTimeField(
        verbose_name=_('Registration date'),
        auto_now_add=True,
        help_text=_('Date and time of registration')
    )
    last_modified = models.DateTimeField(
        verbose_name=_('Last modified'),
        auto_now=True,
        help_text=_('Date and time of profile last modification')
    )
    last_seen = models.DateTimeField(
        verbose_name=_('Last time seen'),
        default=timezone.now,
        help_text=_('Date and time user was last active'),
    )
    whatsapp = models.CharField(
        verbose_name=_('Whatsapp ID'),
        max_length=20,
        blank=True,
        help_text=_('Whatsapp ID with +country_code')
    )
    website = models.URLField(
        verbose_name=_('Website'),
        default='https://sleekforum.com',
        blank=True,
        help_text=_('URL of your website, blog or portfolio')
    )
    repo = models.URLField(
        verbose_name=_('Repo URL'),
        default='https://github.com/',
        blank=True,
        help_text=_('URL to GitHub or Bitbucket')
    )
    facebook = models.URLField(
        verbose_name=_('Facebook URL'),
        default='https://facebook.com/',
        blank=True,
        help_text=_('Facebook Profile URL')
    )
    twitter = models.URLField(
        verbose_name=_('Twitter URL'),
        default='https://twitter.com/@',
        blank=True,
        help_text=_('Twitter URL')
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP Address'),
        blank=True,
        null=True,
        help_text=_('IP Address')
    )


    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='unique_constraint_email_username'
            )
        ]
        indexes = [
            models.Index(
                fields=['id', 'username'],
                name='idx_id_username'
            )
        ]
        ordering = ['email', 'username']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def get_short_name(self):
        return self.username

    @property
    def get_full_name(self):
        fullname = ' '.join([self.firstname, self.middlename, self.lastname])
        return fullname

    @property
    def get_display_name(self):
        if self.firstname or self.lastname:
            return self.get_full_name
        return self.get_short_name

    def last_seen_cache(self):
        return cache.get('seen_%s' % self.username)

    def is_online(self):
        if self.last_seen_cache():
            now = timezone.now()
            if now > self.last_seen_cache() + \
                    datetime.timedelta(seconds=settings.USER_LASTSEEN_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

    @cached_property
    def post_count(self):
        return self.posts.all()

    def get_avatar(self):
        return self.avatar

    def online(self):
        check_online = self.is_online()
        if check_online:
            return 'online'
        return 'offline'

    def get_absolute_url(self):
        kwargs = {
            'username': slugify(self.username)
        }
        return reverse('sleekforum:users:kwarg_home_profile', kwargs=kwargs)

    def __str__(self):
        return '%s - %s' % (self.username, self.email)
