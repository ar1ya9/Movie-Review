from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model= Movies
        fields = ("name","director","cast","description","release","language","image")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ('comment','rating')
