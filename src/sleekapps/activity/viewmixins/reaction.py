from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured, FieldDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin


class ReactionMixin(SingleObjectMixin):
    reaction_model = None
    reaction_field = 'reaction'
    reaction_exclusion = False
    exclude_reactions = ['LIKE', 'DISLIKE']
    reaction = None

    def get_reaction(self, reaction_queryset=None):
        """Return reaction for a user.
        Similar in functionality to django SingleObjectMixin
        """
        if reaction_queryset is None:
            reaction_queryset = self.get_reactions_for_obj(self.object)
        if self.exclude_reactions is True:
            if self.exclude_reactions:
                reaction_field = self.get_reaction_field()
                reaction_queryset = reaction_queryset.exclude(**{
                    reaction_field + str('__in'): self.exclude_reactions
                })
            else:
                raise AttributeError('You cant perform an empty exclusion lookup')
        return reaction_queryset.get(user=self.request.user)

    def get_reaction_field(self):
        """Return validated field name for reaction lookup"""
        if self.reaction_field is None:
            raise ImproperlyConfigured(
                'reaction_field Attribute must be set'
            )
        return self.validate_reaction_field(self.reaction_field)

    def validate_reaction_field(self, field_name):
        """Return validated reaction field for querying."""
        if self.reaction_model is not None:
            fields = [field.name for field in \
                      self.reaction_model._meta.get_fields()]
            if field_name not in fields:
                raise FieldDoesNotExist('Field name for reaction lookup is not valid')
            else:
                return field_name
        else:
            raise ImproperlyConfigured('reaction_model Attribute is missing')

    def get_reactions_for_obj(self, obj):
        """Return all reactions for a given object"""
        reaction_model = self.reaction_model
        return reaction_model.objects.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id
        )


class ReactionView(ReactionMixin, View):
    success_url = ''

    def get(self, request, *args, **kwargs):
        model = self.reaction_model
        self.object = self.get_object()
        self.reactions = self.get_reactions_for_obj(self.object)
        self.field_name = self.get_reaction_field()
        try:
            field_name = self.field_name
            user_reaction = self.get_reaction(self.reactions)
            if getattr(user_reaction, field_name) != self.reaction:
                setattr(user_reaction, field_name, self.reaction)
                user_reaction.save(update_fields=[field_name])
            else:
                user_reaction.delete()
        except self.reaction_model.DoesNotExist:
            create_action = {
                'user': self.request.user,
                'content_object': self.object,
                self.field_name: self.reaction,
            }
            self.reaction_model.objects.create(**create_action)
        return self.get_success_url()

    def get_success_url(self):
        if self.success_url:
            return HttpResponseRedirect(str(self.success_url))
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
