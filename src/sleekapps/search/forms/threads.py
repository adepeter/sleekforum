from django import forms
from django.utils.translation import gettext_lazy as _

from .base import BaseSearchForm


class GlobalThreadSearchForm(BaseSearchForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['keyword'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'size': 10
        })

        if self.request.GET:
            self.fields['keyword'].initial = self.request.GET.get('keyword')
