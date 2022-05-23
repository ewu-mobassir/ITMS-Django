from django import forms
from .models import District


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields=('district_name',)