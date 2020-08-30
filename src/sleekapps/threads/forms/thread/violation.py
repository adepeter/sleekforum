from violation.forms.violation import ViolationForm
from django import forms

from ....cores.fields import RuleField


class ThreadReportForm(ViolationForm):
    categories = ['forum']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rules'] = RuleField(queryset=self.get_queryset(), required=False, widget=forms.RadioSelect)
