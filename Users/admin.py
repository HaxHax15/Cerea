from django.contrib import admin
from .models import Profile,LanguageCode
from .forms import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm

class LanguageCodeAdmin(admin.ModelAdmin):
    form = LanguageCodeForm
    list_display = ('name', 'code',)

admin.site.register(LanguageCode,LanguageCodeAdmin)
admin.site.register(Profile,ProfileAdmin)