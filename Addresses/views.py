from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

@login_required
def countries(request, country_id):
    if not country_id:
        countries_list = Country.objects.all()
    else:
        countries_list = get_list_or_404(Country,pk=country_id)
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

@login_required
def houses(request, house_id):
    houses_list = House.objects.all()
    context = {'houses_list':houses_list}
    return render(request, "tpl/houses.html",context)



def get_name(request,country_id):
    country = get_object_or_404(Country, pk = country_id)
    if request.method == 'POST':
        form = CountryForm(request.POST,instance=country)
        if form.is_valid():
            country = form.save()
            return HttpResponseRedirect('/adminka/locations/countries')
    else:
        form = CountryForm(instance=country)
    return render(request, 'tpl/forms/country_edit_form.html', {'form': form})

def editplace(request,place_id):
    place = get_object_or_404(Country, pk = place_id)
    if request.method == 'POST':
        form = PlaceForm(request.POST,instance=place)
        if form.is_valid():
            country = form.save()
            return HttpResponseRedirect('/adminka/locations/places')
    else:
        form = PlaceForm(instance=place)
    return render(request, 'tpl/forms/place_edit_form.html', {'form': form})