# apps/social_media/forms.py

from django import forms
from .models import User, Photo


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('user', 'photo')
