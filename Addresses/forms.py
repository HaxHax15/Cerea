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
        country = forms.ModelChoiceField(queryset=Country.objects.all(), to_field_name="country")
        region = forms.ModelChoiceField(queryset=Region.objects.all(), to_field_name="region")
        city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name="city")
        street =forms.ModelChoiceField(queryset=Street.objects.all(), to_field_name="street")
        house = forms.ModelChoiceField(queryset=House.objects.all(), to_field_name="house")
        fields = '__all__'
        widgets = {
            'apartments':forms.TextInput(attrs={'class':'form-control'}),
            'latitude':forms.TextInput(attrs={'class':'form-control'}),
            'longitude':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'})
        }


class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }

class StreetForm(forms.ModelForm):

    class Meta:
        model = Street
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }

class HouseForm(forms.ModelForm):

    class Meta:
        model = House
        fields = '__all__'
        widgets = {
            'house': forms.TextInput(attrs={'class':'form-control'}),
            'building': forms.TextInput(attrs={'class': 'form-control'})
        }