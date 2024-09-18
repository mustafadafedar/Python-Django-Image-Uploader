from django import forms
from .models import upload

class imageform(forms.ModelForm):
    class Meta:
        model = upload
        fields = '__all__'
        labels = {'images':''}