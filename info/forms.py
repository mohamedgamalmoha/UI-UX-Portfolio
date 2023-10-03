from django.forms import ValidationError
from django.forms.models import BaseInlineFormSet
from django.utils.translation import gettext_lazy as _

from .enums import LayoutChoices


class CaseStudySectionInlineFormset(BaseInlineFormSet):

    def is_valid(self):
        return super().is_valid() and not any([bool(e) for e in self.errors])

    def clean(self):
        forms = [form for form in self.forms if form.cleaned_data and not form.cleaned_data.get('DELETE', False)]
        instances_with_card_layout = list(
            filter(
                lambda form: form.instance.layout == LayoutChoices.CARD,
                forms
            )
        )
        if len(instances_with_card_layout) // 2 != 0:
            raise ValidationError(
                _(f'Count of instances with card layout should be even not {len(instances_with_card_layout)}')
            )

    def save_new_objects(self, commit=True):
        self.new_objects = []
        offset = max(filter(lambda frm: frm.instance.number is not None, self.initial_forms)) if self.initial_forms \
            else 0
        for index, form in enumerate(self.extra_forms):
            if not form.has_changed() or (self.can_delete and self._should_delete_form(form)):
                continue
            if form.instance.number is None:
                form.instance.number = index + offset
            self.new_objects.append(self.save_new(form, commit=commit))
            if not commit:
                self.saved_forms.append(form)
        return self.new_objects
