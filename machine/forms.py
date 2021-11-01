from django import forms

from .models import Machine
from departement.models import Departement


class MachineModelForm(forms.ModelForm):

    name = forms.CharField(label='Name',
                           widget=forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control", }))

    lastCheckDate = forms.DateField(
        widget=forms.TextInput(attrs={'class': "form-control flatpickr-basic flatpickr-input"}))

    nextCheckDate = forms.DateField(
        widget=forms.TextInput(attrs={'class': "form-control flatpickr-basic flatpickr-input"}))

    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={

                "class": "form-check-input",

            }
        )
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "form-control",

            }
        )
    )

    class Meta:
        model = Machine
        fields = [
            'name',
            'status',
            'lastCheckDate',
            'nextCheckDate',
            'departement',
            'description'


        ]
