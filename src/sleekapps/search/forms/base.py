from django import forms

class BaseSearchForm(forms.Form):
    keyword = forms.CharField(max_length=50)