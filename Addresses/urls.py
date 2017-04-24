from django.conf.urls import url, include
from . import views
urlpatterns=[
    url(r'^countries/(?:(?P<country_id>\d+)/)?$',views.countries, name='countries'),
    #url(r'^regions/$',views.regions, name='regions'),
    #url(r'^cities/$',views.cities, name='cities'),
    #url(r'^streets/$',views.streets, name='streets'),
    #url(r'^houses/$',views.houses, name='houses'),
    #url(r'^places/$',views.places, name='places'),
]