from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def countries(request, country_id):
    countries_list = Country.objects.all()
    context = {'countries_list':countries_list}
    return render(request, "tpl/countries.html",context)

@login_required
def regions(request, region_id):
    regions_list = Region.objects.all()
    context = {'regions_list':regions_list}
    return render(request, "tpl/regions.html",context)

@login_required
def cities(request, city_id):
    cities_list = City.objects.all()
    context = {'cities_list':cities_list}
    return render(request, "tpl/cities.html",context)

@login_required
def streets(request, street_id):
    streets_list = Street.objects.all()
    context = {'streets_list':streets_list}
    return render(request, "tpl/streets.html",context)

@login_required
def places(request, place_id):
    places_list = Place.objects.all()
    context = {'places_list':places_list}
    return render(request, "tpl/places.html",context)

