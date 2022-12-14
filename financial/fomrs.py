from django import forms
from .models import BankAccount


class BankAccountAdminForm(forms.ModelForm):
    class Meta:
        model: BankAccount
        fields: '__all__'

    def clean(self):
        card_number = self.cleaned_data['card_number']
        account_number = self.cleaned_data['account_number']
        sheba = self.cleaned_data['sheba']
        phone_number = self.cleaned_data['phone_number']
        email = self.cleaned_data['email']
        if not card_number and not account_number and not sheba and not phone_number and not email:
            raise forms.ValidationError("One of the last 5 inputs should be filled!")
