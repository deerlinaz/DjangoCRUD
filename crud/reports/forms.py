from django import forms
from . import models

class Create(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = "__all__"

class Delete(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = ['email', 'cname', 'disease_code']

class Update(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = "__all__"