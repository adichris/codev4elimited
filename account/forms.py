from .models import ContactUs
from django import forms
from crispy_forms.helper import FormHelper
from crispy_bulma.layout import FormGroup, Submit, Reset


class ContactUsCreationForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout.append(
            FormGroup(
                Reset('reset', 'Reset'),
                Submit('accept', 'Submit', css_class='is-success'),
            )
        )
        return helper
