from django import forms
from .models import Contact


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model: Contact
        fields: '__all__'

    def clean(self):
        if not self.cleaned_data['firstname'] and not self.cleaned_data['lastname']:
            raise forms.ValidationError("Firstname and Lastname can't be empty in the same time!")
