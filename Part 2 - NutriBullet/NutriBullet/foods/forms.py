from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = ['name', 'slug', 'banner']