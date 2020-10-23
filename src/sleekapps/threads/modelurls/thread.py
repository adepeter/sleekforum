from django.urls import reverse


class ThreadModelURL:
    def get_kwargs(self):
        kwargs = {
            'category_slug': self.category.slug,
            'pk': self.id,
            'slug': self.slug,
        }
        return kwargs

    def get_absolute_url(self):
        return reverse(
            'sleekforum:threads:read_thread',
            kwargs=self.get_kwargs()
        )

    def get_edit_url(self):
        return reverse(
            'sleekforum:threads:edit_thread',
            kwargs=self.get_kwargs()
        )

    def get_delete_url(self):
        return reverse(
            'sleekforum:threads:delete_thread',
            kwargs=self.get_kwargs()
        )

    def get_dislike_url(self):
        return reverse(
            'sleekforum:threads:dislike_thread',
            kwargs=self.get_kwargs()
        )

    def get_like_url(self):
        return reverse(
            'sleekforum:threads:like_thread',
            kwargs=self.get_kwargs()
        )

    def get_sad_url(self):
        return reverse(
            'sleekforum:threads:sad_thread',
            kwargs=self.get_kwargs()
        )

    def get_angry_url(self):
        return reverse(
            'sleekforum:threads:angry_thread',
            kwargs=self.get_kwargs()
        )

    def get_happy_url(self):
        return reverse(
            'sleekforum:threads:happy_thread',
            kwargs=self.get_kwargs()
        )

    def get_love_url(self):
        return reverse(
            'sleekforum:threads:love_thread',
            kwargs=self.get_kwargs()
        )

    def get_wow_url(self):
        return reverse(
            'sleekforum:threads:wow_thread',
            kwargs=self.get_kwargs()
        )

    def get_funny_url(self):
        return reverse(
            'sleekforum:threads:funny_thread',
            kwargs=self.get_kwargs()
        )

    def get_report_url(self):
        return reverse(
            'sleekforum:threads:report_thread',
            kwargs=self.get_kwargs()
        )

    def get_share_url(self):
        return reverse(
            'sleekforum:threads:share_thread',
            kwargs=self.get_kwargs()
        )

    def get_toggle_hide_url(self):
        return reverse(
            'sleekforum:threads:toggle_hide_thread',
            kwargs=self.get_kwargs()
        )

    def get_toggle_lock_url(self):
        return reverse(
            'sleekforum:threads:toggle_lock_thread',
            kwargs=self.get_kwargs()
        )
