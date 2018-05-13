from django import forms
from .models import Image

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
