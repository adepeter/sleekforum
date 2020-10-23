from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from violation.admin import ViolationAdmin as BaseViolationAdmin
from violation.models import Violation as BaseViolationModel

admin.site.unregister(BaseViolationModel)


@admin.register(BaseViolationModel)
class ViolationAdmin(BaseViolationAdmin):
    list_display = BaseViolationAdmin.list_display + ['count_violated_rules']
    def count_violated_rules(self, obj):
        return obj.rules.count()
    count_violated_rules.short_description = _('Total violations')
