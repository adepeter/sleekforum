from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import Category


class BaseCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]
        error_messages = {
            'name': {
                'min_length': 'Too short characters',
                'max_length': 'Too many character enter',
                'required': _('This field must be completed')
            }
        }

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        if self.request.user.owned_blog_categories.filter(name__iexact=cleaned_name).exists():
            raise forms.ValidationError(
                _('%(name)s already exist'),
                code='user_category_name_exists',
                params={'name': cleaned_name}
            )
        return cleaned_name

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.owner = self.request.user
        if commit:
            obj.save()
        return obj


class CategoryCreateForm(BaseCategoryForm):
    pass


class CategoryEditForm(BaseCategoryForm):
    class Meta(BaseCategoryForm.Meta):
        fields = BaseCategoryForm.Meta.fields + [
            'icon',
            'cover',
            'is_hidden',
            'is_locked'
        ]
        labels = {
            'is_hidden': _('Do you wanna hide category?')
        }
        help_texts = {
            'is_hidden': _('If category is hidden, other users will not be view it or access its blog contents')
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Enter a category name')
            })
        }
