from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def countries(request, country_id):
    countr = Country.objects.all()
    s=''
    for c in countr:
        s=s+c.name+'<br>'

    return render(request, "index.html")

