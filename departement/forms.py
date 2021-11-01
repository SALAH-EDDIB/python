from django import forms

from .models import Departement


class DepartementModelForm(forms.ModelForm):

    name = forms.CharField(label='Name',
                           widget=forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control", }))
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
        model = Departement
        fields = [
            'name',
            'description',

        ]
