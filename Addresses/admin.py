# coding: utf8
from django.contrib import admin
from .models import *
from .forms import *


# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    form = CountryForm
    fields = ('name',)


class RegionAdmin(admin.ModelAdmin):
    form = RegionForm
    fields = ('name',)


class CityAdmin(admin.ModelAdmin):
    form = CityForm
    fields = ('name',)


class StreetAdmin(admin.ModelAdmin):
    form = StreetForm
    fields = ('name',)


class HouseAdmin(admin.ModelAdmin):
    form = HouseForm
    fields = ('house', 'building')


class PlaceAdmin(admin.ModelAdmin):
    form = PlaceForm
    fields = ('country ',
              'region ',
              'city',
              'street',
              'house',
              'apartments',
              'latitude',
              'longitude',
              'description',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Street, StreetAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Place, PlaceAdmin)
