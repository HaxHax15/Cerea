from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def countries(request, country_id):
    countries_list = Country.objects.all()
    context = {'countries_list':countries_list}
    return render(request, "tpl/countries.html",context)

def regions(request, region_id):
    regions_list = Region.objects.all()
    context = {'regions_list':regions_list}
    return render(request, "tpl/regions.html",context)

def cities(request, city_id):
    cities_list = City.objects.all()
    context = {'cities_list':cities_list}
    return render(request, "tpl/cities.html",context)

def index(request):
    context = request.user
    return render(request, "tpl/index.html", context)