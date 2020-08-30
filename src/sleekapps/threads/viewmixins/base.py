from django.core.exceptions import ImproperlyConfigured, FieldDoesNotExist


class BooleanObjectMixin:
    """This mixin cannot be implemented on its own.
    Must be called with a view
    """
    boolean_field = ''

    def get_boolean_field(self):
        """Return validated boolean field to be used for action on/off"""
        if not self.boolean_field:
            raise ImproperlyConfigured(
                'You must set boolean_field attribute on this view'
            )
        return self.validate_boolean_field(self.boolean_field)

    def validate_boolean_field(self, boolean_field):
        """Validate boolean field to check if it exists on specified model"""
        fields = [field.name for field in self.model._meta.get_fields()]
        if boolean_field not in fields:
            raise FieldDoesNotExist('%(field_name)s does not seem to be a \
            valid field on the supplied %(model)s' % {
                'model': self.model._meta.model_name,
                'field_name': self.boolean_field})
        else:
            return boolean_field

    def get_boolean_value(self, obj=None):
        """Return existing boolean field value for the obj"""
        if obj is None:
            obj = self.get_object()
        boolean_field = self.get_boolean_field()
        boolean_value = getattr(obj, boolean_field)
        if not isinstance(boolean_value, bool):
            raise TypeError('The returned boolean field value isn\'t a bool')
        return boolean_value

    def toggle_boolean_and_save(self, obj, value=None, value_reverse=True):
        if value is None:
            value = self.get_boolean_value(obj)
        field = self.get_boolean_field()
        new_value = not value if value_reverse else value
        setattr(obj, field, new_value)
        obj.save()
        return obj
