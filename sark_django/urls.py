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
from __future__ import absolute_import
from datetime import date

from django.conf.urls import include, url
from django.contrib import admin
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

from .sark import views

sqs = SearchQuerySet().date_facet('date', start_date=date(1955, 1, 1), end_date=date(2015, 1, 1), gap_by="year").facet('host').facet('performers').facet('instruments').facet('faceted_model_type')

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^demo/$', views.Demo.as_view()),
    url(r'^aboutus/$', views.aboutus),
    url(r'^inventory/$', views.inventory),
    url(r'^aboutmtia/$', views.aboutmtia),
    url(r'^demo/broadcast/([0-9]{4})-([0-9]{2})-([0-9]{2})/', 'sark_django.sark.views.broadcast'),
    url(r'^demo/fieldrecording/(\d*)', 'sark_django.sark.views.field_recording'),
    url(r'^demo/location/([a-zA-Z ]*)\+([a-zA-Z ]*)',  'sark_django.sark.views.location'),
    url(r'^demo/agent/(.*)', 'sark_django.sark.views.agent'),
    url(r'^test/demo',  views.Demo.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^search/', include('haystack.urls')),
    url(r'^search/', views.SarkSearch(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
]


handler404 = 'sark_django.sark.views.error404'
admin.site.site_header = 'Sarkisian Project admin'
