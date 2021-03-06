from django import forms


class RuleField(forms.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return '%(rule_name)s' % {
            'rule_name': obj.name,
        }