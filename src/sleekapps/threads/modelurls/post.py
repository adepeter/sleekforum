from django.urls import reverse


class PostModelURL:

    @property
    def get_kwargs(self):
        kwargs = {
            'thread_slug': self.thread.slug,
            'pk': self.id,
        }
        return kwargs

    def get_absolute_url(self):
        kwargs = {
            'category_slug': self.thread.category.slug,
            'slug': self.thread.slug,
            'pk': self.thread.id
        }
        return reverse(
            'sleekforum:threads:read_thread',
            kwargs=kwargs
        ) + '?page=last'

    def get_edit_url(self):
        return reverse(
            'sleekforum:threads:edit_post',
            kwargs=self.get_kwargs
        )

    def get_delete_url(self):
        return reverse(
            'sleekforum:threads:delete_post',
            kwargs=self.get_kwargs
        )

    def get_reply_to_url(self):
        return reverse(
            'flyapps:threads:post:reply_post',
            kwargs=self.get_kwargs
        )

    def get_dislike_url(self):
        return reverse(
            'sleekforum:threads:dislike_post',
            kwargs=self.get_kwargs
        )

    def get_like_url(self):
        return reverse(
            'sleekforum:threads:like_post',
            kwargs=self.get_kwargs
        )

    def get_wow_url(self):
        return reverse(
            'sleekforum:threads:wow_post',
            kwargs=self.get_kwargs
        )

    def get_happy_url(self):
        return reverse(
            'sleekforum:threads:happy_post',
            kwargs=self.get_kwargs
        )

    def get_angry_url(self):
        return reverse(
            'sleekforum:threads:angry_post',
            kwargs=self.get_kwargs
        )

    def get_sad_url(self):
        return reverse(
            'sleekforum:threads:sad_post',
            kwargs=self.get_kwargs
        )

    def get_love_url(self):
        return reverse(
            'sleekforum:threads:love_post',
            kwargs=self.get_kwargs
        )

    def get_funny_url(self):
        return reverse(
            'sleekforum:threads:funny_post',
            kwargs=self.get_kwargs
        )