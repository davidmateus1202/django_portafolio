from django import forms
from .models import Project

class Postform(forms.ModelForm):

    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'id':'floatingInput',


    }), required=True)
    description = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
        'class':'form-control',
        'id':'floatingTextarea2',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control',
        'type':'file',
        'id':'formFileMultiple',


    }))
    url = forms.URLField(widget=forms.URLInput(attrs={
        'class':'form-control',
        'type':'url',
        'id':'floatingInput',

    }))
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'url']