from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^index.html$', views.adminkaindex, name='adminkaindex'),
    url(r'^locations/', include('Addresses.urls')),

]