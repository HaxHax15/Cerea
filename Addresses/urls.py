from django.conf.urls import url, include
from . import views
urlpatterns=[
    url(r'^countries/(?:(?P<country_id>\d+)/)?$',views.countries, name='countries'),
    url(r'^regions/(?:(?P<region_id>\d+)/)?$',views.regions, name='regions'),
    url(r'^cities/(?:(?P<city_id>\d+)/)?$',views.cities, name='cities'),
    url(r'^streets/(?:(?P<street_id>\d+)/)?$',views.streets, name='streets'),
    #url(r'^houses/$',views.houses, name='houses'),
    url(r'^places/(?:(?P<place_id>\d+)/)?$$',views.places, name='places'),
]