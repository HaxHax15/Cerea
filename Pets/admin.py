# coding: utf8
from django.contrib import admin
from .models import *
# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ('name','owner', 'chip_id')


admin.site.register(PetType)
admin.site.register(PetBreed)
admin.site.register(Pet,PetAdmin)