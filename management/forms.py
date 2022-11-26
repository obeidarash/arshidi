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


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model: Project
        fields: '__all__'

    def clean(self):
        if not self.cleaned_data['fixed_budget'] and not self.cleaned_data['min_budget'] and not self.cleaned_data[
            'max_budget']:
            raise forms.ValidationError("Fixed budget and min / max budget can't be empty in the same time!")

        if self.cleaned_data['fixed_budget'] and self.cleaned_data['min_budget'] and self.cleaned_data['max_budget']:
            raise forms.ValidationError("Fixed budget and min / max budget can't be filled in the same time!")

        if not self.cleaned_data['min_budget'] and self.cleaned_data['max_budget']:
            raise forms.ValidationError("Both min and max budget must be filled!")

        if self.cleaned_data['min_budget'] and not self.cleaned_data['max_budget']:
            raise forms.ValidationError("Both min and max budget must be filled!")

        if self.cleaned_data['min_budget'] > self.cleaned_data['max_budget']:
            raise forms.ValidationError("Min budget cant be greater than Max budget")

        if self.cleaned_data['budget_type'] == 'hour':
            if self.cleaned_data['fixed_budget']:
                raise forms.ValidationError("Budget Type is on Hourly price, you cant fill fixed price")

        if self.cleaned_data['budget_type'] == 'fixed':
            if self.cleaned_data['min_budget'] or self.cleaned_data['max_budget']:
                raise forms.ValidationError(
                    "Budget Type is on Fixed price, you cant fill fixed Min or Max hourly price")
