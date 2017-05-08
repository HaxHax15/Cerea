from django.conf.urls import url, include
from . import views
urlpatterns=[
    url(r'^countries/(?:(?P<country_id>\d+)/)?$',views.countries, name='countries'),
    url(r'^countries/(?:(?P<country_id>\d+)/edit/)?$',views.editcountry, {'title':'Редактирование страну'}),
    url(r'^regions/(?:(?P<region_id>\d+)/)?$',views.regions, name='regions'),
    url(r'^regions/(?:(?P<region_id>\d+)/edit/)?$',views.editregion, {'title':'Редактирование региона'}),
    url(r'^cities/(?:(?P<city_id>\d+)/)?$',views.cities, name='cities'),
    url(r'^cities/(?:(?P<city_id>\d+)/edit/)?$',views.editcity, {'title':'Редактирование города'}),
    url(r'^streets/(?:(?P<street_id>\d+)/)?$',views.streets, name='streets'),
    url(r'^streets/(?:(?P<street_id>\d+)/edit/)?$',views.editstreet, {'title':'Редактирование улицы'}),
    url(r'^houses/(?:(?P<house_id>\d+)/)?$',views.houses, name='houses'),
    url(r'^houses/(?:(?P<house_id>\d+)/edit/)?$',views.edithouse, {'title':'Редактирование дома'}),
    url(r'^places/(?:(?P<place_id>\d+)/)?$',views.places, name='places'),
    url(r'^places/(?:(?P<place_id>\d+)/edit/)?$',views.editplace,{'title':'Редактирование места'}),
]