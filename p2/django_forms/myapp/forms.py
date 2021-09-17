from django import forms
from .models import Snippet, Phonebook
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from phonenumber_field.modelfields import PhoneNumberField


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='Email')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
    phone_number = PhoneNumberField(max_length=12)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'categories',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class='btn-success')
        )


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("name", "body")


class PhonebookForm(forms.ModelForm):
    class Meta:
        model = Phonebook
        fields = ("name", "phone_number")
