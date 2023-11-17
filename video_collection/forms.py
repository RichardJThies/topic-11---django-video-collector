from django import forms
from .models import Video

class VideoForm(forms.ModelForm):#model form in which the user enters their data?
    class Meta:
        model = Video#assigned to be the same as the Video class model
        fields = ['name', 'url', 'notes']

class SearchForm(forms.Form):#regular django form, not related to the db?
    search_term = forms.CharField()#whatever the user inputs

#what does is mean for a form VidoeForm to be a ModelForm vs SearchForm being a Form?


