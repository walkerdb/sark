"""sarkisian_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sark_django.sark import views

urlpatterns = [
    url(r'^$', views.demo, name='home'),
    url(r'^demo/$', views.demo),
    url(r'^aboutus/$', views.aboutus),
    url(r'^inventory/$', views.inventory),
    url(r'^aboutmtia/$', views.aboutmtia),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^program/([0-9]{4})-([0-9]{2})-([0-9]{2})/', views.program),
    url(r'^location/([a-zA-Z]*)\+([a-zA-Z]*)', views.location),
]
