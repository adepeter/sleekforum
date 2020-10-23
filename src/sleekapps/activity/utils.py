from django.utils.html import format_html

from ..cores.helper import get_static

img_class = 'reaction-image reaction-item-dropdown-trigger'

class ReactionIcon:
    def __init__(self, reaction_name, *, path_to_file=None, alt_text=None, klass=None):
        self.name = reaction_name
        icon_name = reaction_name if path_to_file is None else path_to_file
        self.src = self.get_reaction_icon(icon_name)
        self.alt = alt_text if alt_text else self.name
        self.klass = img_class if klass is None else klass

    def get_icon(self):
        img_src = getattr(self, 'src')
        img_alt = getattr(self, 'alt')
        img_class = getattr(self, 'klass')
        return format_html('<img src="{}" alt="{}" class="{}" />', img_src, img_alt, img_class)

    def __str__(self):
        return self.get_icon()

    def get_reaction_icon(self, file):
        return get_static(f'img/reactions/{file}.png')
