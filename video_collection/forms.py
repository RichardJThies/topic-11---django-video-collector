from django import forms
from .models import Video

class VideoForm(forms.ModelForm):#model form inwhich the user enters their data?
    class Meta:
        model = Video#assihned to be the same as the Video class model
        fields = ['name', 'url', 'notes']
















