from django import forms
from .models import Project, TimeSheet


class TimeSheetAdminForm(forms.ModelForm):
    class Meta:
        model: TimeSheet
        fields: '__all__'

    def clean(self):
        if not self.cleaned_data['payment_hourly'] and not self.cleaned_data['payment_fixed']:
            raise forms.ValidationError("payment_hourly and payment_fixed can't be empty in the same time!")

    # this validator is not working, and I don't know why

