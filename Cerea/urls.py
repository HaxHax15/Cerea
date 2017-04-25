# coding: utf8
"""Cerea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
import django.contrib.auth.views
import app.forms
import app.views
from django.conf import settings

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^login/$',app.views.LoginFormView.as_view()),
    url(r'^logout$',app.views.LogoutView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^adminka/', include('app.urls')),
    url(r'', include('app.urls')),
    url(r'index.html', include('app.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
