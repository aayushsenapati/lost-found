from django import forms
from .models import *


class ReportForm(forms.ModelForm):
    class Meta:
        model = Reported
        fields = ['name', 'description', 'image']