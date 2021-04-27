from django import forms
from django.utils.translation import gettext_lazy as _


class ArticleSearchForm(forms.Form):
    search = forms.CharField(
        label=_('Search article')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
