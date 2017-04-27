from django import forms
from .models import *

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }

class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = '__all__'

class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = '__all__'
