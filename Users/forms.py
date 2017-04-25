from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','location','location','birth_date','avatar', 'languagecode')


class LanguageCodeForm(forms.ModelForm):
    class Meta:
        model = LanguageCode
        fields = ('name', 'code')