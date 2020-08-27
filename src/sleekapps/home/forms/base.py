from django.utils.text import slugify

from ...threads.forms.thread.thread import ThreadCreationForm


class HomepageThreadCreationForm(ThreadCreationForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    class Meta(ThreadCreationForm.Meta):
        fields = ThreadCreationForm.Meta.fields + ['category', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.starter = self.user
        if commit:
            instance.save()
        return instance
