# coding: utf8
from django.contrib import admin
from .models import *
from .forms import CountryForm,PlaceForm
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    form = CountryForm
    fields = ('name',)




admin.site.register(Country,CountryAdmin)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(House)
admin.site.register(Place)