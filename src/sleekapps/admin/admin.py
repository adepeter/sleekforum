from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class SleekForumAdmin(admin.AdminSite):
    title_header = _('SleekForum Admin')
    site_header = _('SleekForum Administration')
